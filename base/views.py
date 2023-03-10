from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Channel, Topic, Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ChannelForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# channels = [
#     {'id': 1, 'name': 'Recipes'},
#     {'id': 2, 'name': 'Politics'},
#     {'id': 3, 'name': 'Social Activities'},
#     {'id': 4, 'name': 'Sport'},
#     {'id': 5, 'name': 'SlackBay'},
# ]


# Created views
def loginView(request):

    if request.user.is_authenticated:
        return redirect('home')

    # only login is a django function. would produce an error
    if request == 'POST':
        # of form in register_login

        username = request.POST.get('username')
        password = request.POST.get('password')
        # these 2 values will be sent from the frontend

        try:
            user = User.objects.get(username=username)
            # to check if the user exists (User was imported)
        except ValueError:
            messages.error(request, 'Wrong Username. Try again!')
            # this message is an imported django message

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Username or Password. Try again!')

    context = {}
    return render(request, 'base/register_login.html', context)


def home(request):
    r = request.GET.get('r') if request.GET.get('r') is not None else ''
    # r = request.GET.get('r') if request.GET.get('r') != None else ''

    queryset = Channel.objects.filter(
        Q(topic__title__icontains=r) |
        Q(title__icontains=r) |
        Q(content__icontains=r)
    )
    # this filters by Channel-topic-title (the__ takes the parent of topic)
    # Or (|) other model attributes
    # icontains means that r schouls at least be in the name.
    # i means it doesnt metter if small or big letters
    # queryset = Channel.objects.all()
    # puts all objects in the model to context to render in index.html
    topics = Topic.objects.all()
    channel_count = topics.count()
    comments = Post.objects.all().order_by('-created_on').filter(
        Q(channel__topic__title__icontains=r))
    # this filters by the title of the topic of the channel
    # if the url ending is in channel title

    context = {
        'channels': queryset, 'topics': topics,
        'channel_count': channel_count, 'comments': comments}
    return render(request, 'base/index.html', context)


def userAccount(request, pk):
    queryset = User.objects.get(id=pk)
    user_channels = queryset.channel_set.all()
    # this gives the whole Channel Model of the User with the right id
    # channels in context need to be called channels
    # because channel_availiable.html asks for channels!
    user_comments = queryset.post_set.all()
    catgories = Topic.objects.all()

    context = {'user': queryset, 'channels': user_channels,
               'comments': user_comments, 'topics': catgories}
    return render(request, 'base/account.html', context)


def channel(request, pk):
    queryset = Channel.objects.get(id=pk)
    # puts the Channel-object (created in the admin panel) with the id
    # into context. django gives all objects a id by default
    posts = queryset.post_set.all().order_by('-created_on')
    # this gives all attributes of the Channel-Model-Child Post
    # (post in lower case!)
    guests = queryset.guests.all()
    # .all because it's a many to many relationship

    if request.method == 'POST':
        post = Post.objects.create(
            user=request.user,
            channel=queryset,
            body=request.POST.get('body'),
        )
        # Post was imported, create is a django function

        queryset.guests.add(request.user)
        # this makes everybody a guest of the channel who posts something

        return redirect('channel', pk)

    context = {'channel': queryset, 'posts': posts, 'guests': guests}
    return render(request, 'base/channel.html', context)


# def channel(request, pk):
#     channel = None
#     for i in channels:
#         if i['id'] == int(pk):
#             channel = i
#     context = {'channel': channel}
#     return render(request, 'base/channel.html', context)

@login_required(login_url='/accounts/login/')
def createChannel(request):
    form = ChannelForm()

    if request.method == 'POST':
        # method of the form in channel_form.html
        # print(request.POST)
        # gets the result in the terminal - indead >
        form = ChannelForm(request.POST)
        # this passis the POST into the form automatically.
        if form.is_valid():
            channel = form.save(commit=False)
            channel.host = request.user
            channel.save()
            # once a valid form is saved i want to redirect to home(index) page
            # the url name is targeted
            # commir=False pevents the form values to get saved automaticly
            # then you can still change values you need to change.
            # now i want to show the updated form in another html > new view!
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/channel_form.html', context)


@login_required(login_url='/accounts/login/')
def updateChannel(request, pk):
    queryset = Channel.objects.get(id=pk)
    form = ChannelForm(instance=queryset)
    # this shows the prefild form to edit (instance is important!)

    # if request.user != Channel.host:
    if request.user != queryset.host:
        return HttpResponse('You are not authorized!')

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

@login_required(login_url='/accounts/login/')
def deleteChannel(request, pk):
    object = Channel.objects.get(id=pk)

    if request.user != object.host:
        return HttpResponse('You are not authorized!')

    context = {'object': object}
    if request.method == 'POST':
        object.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)


@login_required(login_url='/accounts/login/')
def deleteComment(request, pk):
    object = Post.objects.get(id=pk)

    # if request.user != object.host:
    # if request.user != object.user:
    #     return HttpResponse('You are not authorized!')

    context = {'object': object}
    if request.method == 'POST':
        object.delete()
        return redirect('home')
        # return redirect('channel', Post.channel__id)
    return render(request, 'base/delete.html', context)


def base2(request):

    context = {}
    return render(request, 'base/base2.html', context)