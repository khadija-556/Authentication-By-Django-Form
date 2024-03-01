from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from myApp.forms import *

# Create your views here.

def singinPage(request):
    if request.method == 'POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            
            user=authenticate(username =username,password = password)
            login(request,user)
            return redirect("homePage")
    else:
            form=LoginForm()

    
    
    return render(request,'singin.html',{'form':form})

def singupPage(request):
    if request.method == 'POST':
        form=customUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(singinPage)
    else:
        form=customUserForm()
        
    
    return render(request,'singup.html',{'form':form})
def homePage(request):
    return render(request, "home.html")
def logoutPage(request):
    logout(request)
    return redirect("singinPage")
