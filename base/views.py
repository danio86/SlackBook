from django.shortcuts import render


channels = [
    {'id': 1, 'name': 'Recipes'},
    {'id': 2, 'name': 'Politics'},
    {'id': 3, 'name': 'Social Activities'},
    {'id': 4, 'name': 'Sport'},
    {'id': 5, 'name': 'SlackBay'},
]


# Created views
def home(request):
    context = {'channels': channels}
    return render(request, 'base/index.html', context)


def channel(request, pk):
    channel = None
    for i in channels:
        if i[id] == int(pk):
            channel = i
    context = {'channel': channel}
    return render(request, 'base/channel.html', context)
