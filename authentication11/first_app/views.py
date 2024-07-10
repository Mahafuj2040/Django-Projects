from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('homepage')  # Redirect to the same page or any other page
        else:
            form = RegisterForm()

        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')
        
    
    

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name, password = user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else:
        return redirect('profile')
        
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    
    else:
        return redirect('login')
        

def change_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Updated Successfully')
                return redirect('profile')  # Redirect to the same page or any other page
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'change_data.html', {'form': form})
    else:
        return redirect('signup')
    
    
def user_logout(request):
    logout(request)
    messages.success(request, 'Loggout Successfully')
    return redirect('login')



def pass_change(request):
    if request.user.is_authenticated:  # Correct the authentication check
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Updated Password
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:  # Correct the authentication check
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Updated Password
                messages.success(request, 'Password set successfully')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passchange.html', {'form': form})
    else:
        return redirect('login')
    
    
