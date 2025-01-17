from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, 
                                        email=email)
        return JsonResponse({"message": "User registered successfully"}, status=201)
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return JsonResponse({"message": "User logged in Successfully"})
        return JsonResponse({"message": "Invalid credentials"}, status=401)
    

