from django.urls import path
from . import views


urlpatterns = [
    path('register_login/', views.loginView, name='register_login'),
    path('', views.home, name='home'),
    path('user-account/<str:pk>/', views.userAccount, name='user-account'),
    path('channel/<str:pk>/', views.channel, name='channel'),
    # channel.html can now dynamically access
    # a string (could also be slug, int,...)
    # pk= primary key (that will be appended to the url)
    # this needs to be addited to the channel-arguments in views.py
    path('create-channel/', views.createChannel, name='create-channel'),
    # url don't need the name of the html
    path(
     'update-channel/<str:pk>/', views.updateChannel, name='update-channel'),
    path(
     'delete-channel/<str:pk>/', views.deleteChannel, name='delete-channel'),
    # path('register_login/', views.loginView, name='register_login'),
    path(
     'delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),
    
    path('base2/', views.base2, name='base2'),
]
