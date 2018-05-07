from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('credentials:main')
    else:
        form = UserCreationForm()
    return render(request, 'credentials/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('credentials:main')
        user = form.get_user()
        login(request, user)
    else:
        form = AuthenticationForm()
        return render(request, 'credentials/login.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'credentials/logout.html')


def main(request):
    if request.method == 'POST':
        main(request)
    return render(request, 'credentials/main.html')






