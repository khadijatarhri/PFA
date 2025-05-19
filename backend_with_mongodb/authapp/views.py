from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from db_connections import db
from django.contrib.auth.hashers import make_password, check_password

users = db["users"]

# === Vues REST ===
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if users.find_one({"email": data["email"]}):
            return Response({"message": "Email already exists"}, status=400)
        data["password"] = make_password(data["password"])
        users.insert_one(data)
        return Response({"message": "User registered successfully"}, status=201)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        user = users.find_one({"email": data["email"]})
        if user and check_password(data["password"], user["password"]):
            return Response({"message": "Login successful"}, status=200)
        return Response({"message": "Invalid credentials"}, status=401)

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Home page!"})

# === Vues HTML classiques ===
def login_page(request):
    return render(request, 'authapp/login.html')

def register_page(request):
    return render(request, 'authapp/register.html')

def home_page(request):
    return render(request, 'authapp/home.html')
