from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('channel/<str:pk>/', views.channel, name='channel')
    # channel.html can now dynamically access
    # a string (could also be slug, int,...)
    # pk= primary key (that will be appended to the url)
    # this needs to be addited to the channel-arguments in views.py
]
