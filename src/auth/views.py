from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, "auth/login.html")

def register_view(request):
    return render(request, "auth/login.html")