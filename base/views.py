from django.shortcuts import render, redirect
from .models import Channel, Topic
from .forms import ChannelForm

# channels = [
#     {'id': 1, 'name': 'Recipes'},
#     {'id': 2, 'name': 'Politics'},
#     {'id': 3, 'name': 'Social Activities'},
#     {'id': 4, 'name': 'Sport'},
#     {'id': 5, 'name': 'SlackBay'},
# ]


# Created views
def home(request):
    r = request.GET.get('r') if request.GET.get('r') is not None else ''
    # r = request.GET.get('r') if request.GET.get('r') != None else ''

    queryset = Channel.objects.filter(topic__title__icontains=r)
    # this filters by Channel-topic-title (the__ takes the parent of topic)
    # icontains means that r schouls at least be in the name.
    # i means it doesnt metter if small or big letters
    # queryset = Channel.objects.all()
    # puts all objects in the model to context to render in index.html
    topics = Topic.objects.all()
    context = {'channels': queryset, 'topics': topics}
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
    form = ChannelForm()
    if request.method == 'POST':
        # method of the form in channel_form.html
        # print(request.POST)
        # gets the result in the terminal - indead >
        form = ChannelForm(request.POST)
        # this passis the POST into the form automatically.
        if form.is_valid():
            form.save()
            # once a valid form is saved i want to redirect to home(index) page
            # the url name is targeted
            # now i want to show the updated form in another html > new view!
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/channel_form.html', context)


def updateChannel(request, pk):
    queryset = Channel.objects.get(id=pk)
    form = ChannelForm(instance=queryset)
    # this shows the prefild form to edit (instance is important!)
    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=queryset)
        # this only updates the form. It doesn't refill it.
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/channel_form.html', context)


# def deleteChannel(request, pk):
#     queryset = Channel.objects.get(id=pk)
#     queryset.delete()
#     return redirect('home')
# this works but any user could delete every channel

def deleteChannel(request, pk):
    object = Channel.objects.get(id=pk)
    context = {'object': object}
    if request.method == 'POST':
        object.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)
