from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.middleware.csrf import get_token
from .db import col

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Simple MongoDB query to check if the user exists
        user = col['users'].find_one({'username': username, 'password': password})

        if user:
            return HttpResponse(f"Welcome {user['username']}")
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'users/login.html', {'csrf_token': get_token(request)})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Insert new user into MongoDB
        col['users'].insert_one({'username': username, 'password': password})
        return redirect('login')

    return render(request, 'users/register.html', {'csrf_token': get_token(request)})
