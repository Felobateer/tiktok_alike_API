from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Register User
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password or not email:
            return JsonResponse({"error": "All fields are required."}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({"message": "User registered successfully"}, status=201)
    return HttpResponseNotAllowed(['POST'])

# Login User
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({"error": "Both username and password are required."}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "User logged in successfully"})
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    return HttpResponseNotAllowed(['POST'])

# Placeholder for Token Authentication (custom logic needed)
def authenticate_user(token):
    
    # Implement your token authentication logic here
    return JsonResponse({"error": "Token authentication is not implemented."}, status=501)
