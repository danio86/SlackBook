from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('channel/<str:pk>/', views.channel, name='channel'),
    # channel.html can now dynamically access
    # a string (could also be slug, int,...)
    # pk= primary key (that will be appended to the url)
    # this needs to be addited to the channel-arguments in views.py
    path('create-channel/', views.createChannel, name='create-channel'),
    # url don't the name of the html
    path(
     'update-channel/<str:pk>/', views.updateChannel, name='update-channel'),
]
