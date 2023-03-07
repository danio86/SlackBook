from django.shortcuts import render
from .models import Channel


# channels = [
#     {'id': 1, 'name': 'Recipes'},
#     {'id': 2, 'name': 'Politics'},
#     {'id': 3, 'name': 'Social Activities'},
#     {'id': 4, 'name': 'Sport'},
#     {'id': 5, 'name': 'SlackBay'},
# ]


# Created views
def home(request):
    queryset = Channel.objects.all()
    # puts all objects in the model to context to render in index.html
    context = {'channels': queryset}
    return render(request, 'base/index.html', context)


def channel(request, pk):
    queryset = Channel.objects.get(id=pk)
    # puts the Channel-object (created in the admin panel) with the id 
    # into context. django gives all objects a id by default
    context = {'channel': queryset}
    return render(request, 'base/channel.html', context)


# def channel(request, pk):
#     channel = None
#     for i in channels:
#         if i['id'] == int(pk):
#             channel = i
#     context = {'channel': channel}
#     return render(request, 'base/channel.html', context)


def createChannel(request):
    """ queryset = Channel.objects.get(id=pk) """

    context = {}
    return render(request, 'base/channel_form.html', context)