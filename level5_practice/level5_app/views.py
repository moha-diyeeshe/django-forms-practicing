from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from level5_app.forms import UserForm, UserProfileInfoForm

# Create your views here.

def index(request):
    return render(request,'level5_App/index.html')

def registration(request):
    registered = False

    if request.method == 'POST':  # Note the capitalization here
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'level5_app/registration.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('level5_app:index'))







def user_login(request):

    print("attempting to log")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request,'level5_app/inside.html')  # Redirect to the home page
            else:
                return HttpResponse("Account is not active")
        else:
            print("Someone tried to login and failed")
            print(f'Username: {username} Password: {password}')
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'level5_app/login.html')
