from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from django.http import JsonResponse, HttpResponse

# instantiate pusher
pusher = Pusher(app_id=u'XXX_APP_ID', key=u'XXX_APP_KEY', secret=u'XXX_APP_SECRET', cluster=u'XXX_APP_CLUSTER')
# Create your views here.
#add the login required decorator, so the method cannot be accessed withour login
@login_required(login_url='login/')
def index(request):
    return render(request,"chat.html");

#use the csrf_exempt decorator to exempt this function from csrf checks
@csrf_exempt
def broadcast(request):
    # collect the message from the post parameters, and save to the database
    message = Conversation(message=request.POST.get('message', ''), status='', user=request.user);
    message.save();
    # create an dictionary from the message instance so we can send only required details to pusher
    message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
    #trigger the message, channel and event to pusher
    pusher.trigger(u'a_channel', u'an_event', message)
    # return a json response of the broadcasted message
    return JsonResponse(message, safe=False)

#return all conversations in the database
def conversations(request):
    data = Conversation.objects.all()
    # loop through the data and create a new list from them. Alternatively, we can serialize the whole object and send the serialized response 
    data = [{'name': person.user.username, 'status': person.status, 'message': person.message, 'id': person.id} for person in data]
    # return a json response of the broadcasted messgae
    return JsonResponse(data, safe=False)

#use the csrf_exempt decorator to exempt this function from csrf checks
@csrf_exempt
def delivered(request, id):
 
    message = Conversation.objects.get(pk=id);
    # verify it is not the same user who sent the message that wants to trigger a delivered event
    if request.user.id != message.user.id:
        socket_id = request.POST.get('socket_id', '')
        message.status = 'Delivered';
        message.save();
        message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
        pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
        return HttpResponse('ok');
    else:
        return HttpResponse('Awaiting Delivery');
