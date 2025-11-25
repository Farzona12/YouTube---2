from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='login')
def channel_create_view(request):
    if request.method == "GET":
        return render(request,'channel_create.html')
    elif request.method =='POST':
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        image = request.FILES.get('image', None)
        if not title:
            return render(request,'channel_create.html', context={'title':title,'description':description, 'error':'Title is required'})
        channel =Channel(title=title, description=description, image=image, owner = request.user)
        channel.save()
        return redirect('channel_list')



def channel_list_view(request):
    channels = Channel.objects.filter(owner=request.user)
    videos = Video.objects.filter(channel__in=channels)
    posts = Post.objects.filter(channel__in=channels)
    

    return render(request, 'channel_list.html', {
        "channels": channels,
        "videos": videos,
        "posts": posts})
    
def channel_detail_view(request, pk):
    channel = Channel.objects.filter(id=pk).first()
    is_subscribed = request.user in channel.subscribers.all()

    if request.method == "POST":
        if "unsubscribe" in request.POST:
            channel.subscribers.remove(request.user)
        elif "subscribe" in request.POST:
            channel.subscribers.add(request.user)
        return redirect("channel_detail", pk=pk)

    videos = channel.video_set.all()
    posts = channel.post_set.all()

    return render(request, "channel_detail.html", {
        "channel": channel,
        "videos": videos,
        "posts": posts,
        "is_subscribed": is_subscribed,
    })
    
def channel_update_view(request, pk):
    channel = Channel.objects.filter(owner = request.user, id = pk)
    if request.method =='GET':
        return render(request,'channel_update.html', context={'channel':channel, 'what_can_do':'You can change the prifile of your channel'} )
    elif request.method =="POST":
        title = request.POST.get('title', channel.title)
        description = request.POST.get('description', channel.description)
        image = request.FILES.get('image',channel.image)
        channel.title = title
        channel.description = description
        channel.image = image
        channel.save()
        return redirect('channel_list')

def channel_delete_view(request,pk):
    channel = Channel.objects.filter(owner = request.user, id = pk).first()
    if request.method == 'GET':
        return render(request, 'channel_delete_confirm.html', context={'channel':channel})
    if request.method =='POST':
        answer = request.POST.get('answer', None)
        if answer == 'delete':
            channel.delete()
            return redirect('channel_list')
        elif answer == 'cancel':
            return redirect('channel_list')
        
def post_create_view(request, pk):
    channel = Channel.objects.filter(id = pk).first()
    if request.user!= channel.owner:
        return render(request, 'channel_create.html', context={'error_channel':'You are not the owner of this channel'})        
    if request.method == "GET":
        return render(request, 'post_create.html')
    elif request.method == 'POST':
        content = request.POST.get('content', None)
        image = request.FILES.get('image', None)
        print(image)
        video = request.FILES.get('video', None)
        print(video)
        if not image and not video:
            return render(request, 'post_create.html', context={'content':content, 'error':'You should post or image or video'})
        post = Post(channel = channel, content=content, image = image, video= video)
        post.save()
        return redirect('channel_detail', pk=pk)
    
    
def video_create_view(request, pk):
    print('first')
    channel = Channel.objects.filter(id = pk).first()
    if not channel:
        return render(request, 'video_create.html', context={'error_channel':'Such channels does not exists'})        
        
    if request.user != channel.owner:
        return render(request, 'video_create.html', context={'error_channel':'You are not the owner of this channel'})        
    
    if request.method == "GET":
        return render(request, 'video_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        description = request.POST.get('description', None)
        video_file = request.FILES.get('video_file', None)
        is_public= request.POST.get('is_public', None) == 'on'
        if  not video_file:
            return render(request, 'video_create.html', context={'title':title, 
                                                                'error':'You should send a video',
                                                                'description':description})
        video = Video(is_public=is_public,channel = channel, title=title, video_file = video_file, description= description)
        video.save()
        return redirect('channel_detail', pk=pk)
        