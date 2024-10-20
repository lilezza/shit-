from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required ,user_passes_test

# Create your views here.
@login_required
def profile(requset):
    return render(requset , 'accounts/profile.html')

@user_passes_test(lambda user:not user.is_authenticated , '/' , None)
def register(requset):
    if requset.method == 'POST':
        form = UserCreationForm(requset.POST)
        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = UserCreationForm()

    return render(requset , 'registration/register.html' , { 'form' : form})
def user_logout(request):
    logout(request)

    return render(request , 'registration/accountlogout.html')
