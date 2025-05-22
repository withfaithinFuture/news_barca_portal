from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def history(request):
    return render(request, 'history.html')

def squad(request):
    return render(request, 'squad.html')

def profile(request):
    return render(request, 'profile.html')

def auth_view(request):
    return render(request, 'registration/auth.html')

def register_view(request):
    return render(request, 'registration/register.html')
