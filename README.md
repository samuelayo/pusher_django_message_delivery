# BUILD READ RECEIPTS USING DJANGO

Today, we will make a read receipt framework for your chat app with Django and Pusher. The full tutorial can be found here : https://pusher.com/tutorials/read-receipts-django/](https://pusher.com/tutorials/read-receipts-django/) 

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
### Prerequisites

#### Setup Pusher

If you don't have one already, create a free Pusher account at https://pusher.com/signup then login to your dashboard and create an app. 


- Replace the XXX_APP_ID, XXX_APP_KEY, XXX_APP_SECRET and XXX_APP_CLUSTER with your own keys you obtained when you created an app on Pusher in the line below in your `message\views.py` file. If you dont have a Pusher account, sign up [here](Https://pusher.com) 
```
Pusher(app_id=u'XXX_APP_ID', key=u'XXX_APP_KEY', secret=u'XXX_APP_SECRET', cluster=u'XXX_APP_CLUSTER')
```
- Replace the XXX_APP_KEY with your app key in the `message\templates\chat.html` file.

#### Database Migrations
 - Run the following command at the root of your application to  make the migrations needed for the database
 
 ```
 python manage.py makemigrations
 ```
 
 - Run this command to migrate the database
 
 ```
  python manage.py migrate
 ```
- Create two super users by running the below command twice:
```
python manage.py createsuperuser
```

And finally, start the application:

```
python manage.py runserver.
```
and visit http://localhost:8000/ to see the application in action.


## Built With

* [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
* [DJango](https://docs.djangoproject.com/) - The web framework for perfectionists with deadlines. 
* [Vue.js](https://vuejs.org/) - The Progressive JavaScript Framework.

