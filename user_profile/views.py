from django.shortcuts import render, redirect, HttpResponse
from .models import User_profile
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def profile_create_view(request):
    if request.method == 'GET':
        return render(request, 'profile_create.html')
    elif request.method == 'POST':
        image = request.FILES.get('image', None)
        bio = request.POST.get('bio', None)
        age = request.POST.get('age', None)
        if not image:
            return render(request, 'profile_create.html', context={
                                                                   'bio':bio,
                                                                   'age':age,
                                                                  'error':'Image is reqired !'
                                                                })
        if not age:
            return render(request, 'profile_create.html', context={
                                                                   'bio':bio,
                                                                   'age':age,
                                                                  'error':'Age is reqired !'
                                                                })
        profile= User_profile(image = image , bio=bio, age=age, user= request.user)
        profile.save()
        return HttpResponse('create done')




@login_required(login_url='login')
def profile_update_view(request ,pk):
    profile = User_profile.objects.filter(id = pk).first()
    if request.method == 'GET':
        if profile.user!=request.user:
            return HttpResponse('You cannot delete this profile')
    
        if profile:
            return render(request, 'profile_update.html', context={'profile':profile})
        elif not profile:
            return HttpResponse('Could not find  this profile ☹️ ')
    elif request.method == 'POST':
        image = request.FILES.get('image', profile.image)
        bio = request.POST.get('bio', profile.bio)
        age = request.POST.get('age', profile.age)
        profile.image  =image
        profile.bio  =bio
        profile.age  =age
        profile.save()
        return HttpResponse('update done')
    
    
@login_required(login_url='login')
def profile_delete_view(request, pk):
    profile = User_profile.objects.filter(id=pk).first()
    if not profile:
        return HttpResponse('Could not find this profile ☹️')

    if request.method == 'POST':
        if request.POST.get('confirm') == 'delete':
            profile.delete()
            return redirect('profile_list') 
        elif request.POST.get('confirm') == 'cancel':
            return redirect('profile_list')  
    if profile.user!=request.user:
        return HttpResponse('You cannot delete this profile')
    
    return render(request, 'confirm_delete.html', {'profile': profile})
        


def profile_list_view(request):
    profile  =User_profile.objects.all()
    if profile:
        return render(request, 'profile_list.html', context={'profile':profile})
    elif not profile :
        return HttpResponse("No profiles found")


