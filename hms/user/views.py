from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import NewGuestRegister
def home(response):
    return render(response, "user/base.html", {})

def guest_register(response):
    if response.method == "POST":
        form = NewGuestRegister(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/user/")
        else:
            form = NewGuestRegister()
            return render(response, "user/guest_register.html", {"form":form})
    else:
        form = NewGuestRegister()
        return render(response, "user/guest_register.html", {"form":form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('************')
        print(username, password)
        print('************')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is inactive")
        else:
            print("Someone tried to login and failed.")
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'registration/login.html', {})