# Message Delivery Status With Pusher
Building a realtime message delivery status using Django and Pusher
## Getting Started
- clone this repository by running: 
```
git clone https://github.com/samuelayo/pusher_django_message_delivery.git
```
- Change directory to the cloned repo
```
cd django_message_delivery
```
- install required libraries: i.e pusher and django
```
pip install django pusher
```
- replace the XXX_APP_ID, XXX_APP_KEY, XXX_APP_SECRET and XXX_APP_CLUSTER with your own keys you obtained when you created an app on Pusher in the line below in your `message\views.py` file. If you dont have a Pusher account, sign up [here](Https://pusher.com) 
```
Pusher(app_id=u'XXX_APP_ID', key=u'XXX_APP_KEY', secret=u'XXX_APP_SECRET', cluster=u'XXX_APP_CLUSTER')
```
- replace the XXX_APP_KEY with your app key in the `message\templates\chat.html` file.

- Create two super users by running the below command twice:
```
python manage.py createsuperuser
```
- Finally, run the application:
```
python manage.py runserver
```