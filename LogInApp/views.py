from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from LogInApp.forms import SignUpForm, User_Profile_Change, Profile_Pic
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method=='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            
    diction = {'form':form, 'registered':registered}
    return render(request, 'LogInApp/signup.html', context=diction)


def log_in(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
    
    diction={'form':form}
    return render(request, 'LogInApp/login.html', context=diction)


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    diction = {}
    return render(request, 'LogInApp/profile.html', context=diction)


@login_required
def user_change(request):
    current_user = request.user
    form = User_Profile_Change(instance=current_user)
    if request.method == 'POST':
        form = User_Profile_Change(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = User_Profile_Change(instance=current_user)
    
    diction = {'form': form}
    return render(request, 'LogInApp/user_change.html', context=diction)


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method=='POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
            
    
    diction = {'form': form, 'changed': changed}
    return render(request, 'LogInApp/change_pass.html', context=diction)


@login_required
def add_profile_pic(request):
    form = Profile_Pic()
    if request.method=='POST':
        form=Profile_Pic(request.POST, request.FILES)
        if form.is_valid():
            user_obj= form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('LogInApp:profile'))
    diction = {'form': form}
    return render(request, 'LogInApp/add_profile_pic.html', context=diction)


@login_required
def change_pro_pic(request):
    form = Profile_Pic(instance=request.user.user_profile)
    
    if request.method == 'POST':
        form = Profile_Pic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LogInApp:profile'))
    
    diction = {'form': form}
    return render(request, 'LogInApp/add_profile_pic.html', context=diction)