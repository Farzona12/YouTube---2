from django.shortcuts import redirect, render, HttpResponse
from .models import *
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password



def register_view(request):
    if request.method == "GET":
        return render(request, "register.html")
    
    elif request.method == "POST":

        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        confirm_password = request.POST.get("confirm_password", None)

        if not username or not email or not password:
            return render(request, "register.html", context={
                "username": username,
                "email": email,
                "error": "Все поля важны! Пожалуйста заполните все поля."
            })


        if password != confirm_password:
            return render(request, "register.html", context={
                "username": username,
                "email": email,
                "error": "Ваш пароль не совпадает!"
            })

        hash_password = make_password(password)

        user = CustomUser(username=username, email=email, password=hash_password)
        try:
            user.save()
            return redirect("/login/")
        except :
            return render(request, "register.html", context={
            "username": username,
            "email": email,
            "error": "Пользователь с этим email уже существует!"})



def login_view(request):

    if request.method == "GET":
        return render(request, "login.html")
    
    elif request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        if not email or not password:
            return render(request, "login.html", context={
                "email": email,
                "error": "Все поля важны! Пожалуйста заполните все поля."
            })

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user=user)
            return redirect("/home/")
        
        return render(request, "login.html", context={
            "email": email,
            "error": "Ваши данные неправильные!"
        })



def logout_view(request):

    try:
        logout(request)

    except Exception as err:
        return HttpResponse(str(err))
    
    return redirect("/login/")

