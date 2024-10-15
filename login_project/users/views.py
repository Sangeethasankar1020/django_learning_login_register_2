from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.middleware.csrf import get_token
from .db import col



questions = [
    {"id": 1, "question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct": "Paris"},
    {"id": 2, "question": "Who wrote '1984'?", "options": ["George Orwell", "Aldous Huxley", "Ernest Hemingway", "F. Scott Fitzgerald"], "correct": "George Orwell"},
    {"id": 3, "question": "What is the largest planet in the Solar System?", "options": ["Earth", "Jupiter", "Saturn", "Mars"], "correct": "Jupiter"},
    {"id": 4, "question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "1,000,000 km/s", "30,000 km/s"], "correct": "300,000 km/s"},
    {"id": 5, "question": "What is the symbol for gold in the periodic table?", "options": ["Ag", "Au", "Pb", "Pt"], "correct": "Au"},
]

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Simple MongoDB query to check if the user exists
        user = col['users'].find_one({'username': username, 'password': password})

        if user:
            return redirect('dashboard') 
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




# Dashboard view to display questions
def dashboard_view(request):
    if request.method == 'POST':
        # Get the answers from POST and pass them to the result page
        answers = request.POST
        return render(request, 'users/result.html', {'questions': questions, 'answers': answers})
    return render(request, 'users/dashboard.html', {'questions': questions})

# Result view to show the correct and incorrect answers
def result_view(request):
    if request.method == 'POST':
        # Process the answers submitted via POST
        answers = request.POST
        results = []
        for q in questions:
            user_answer = answers.get(f"q{q['id']}")
            correct = user_answer == q['correct']
            results.append({
                'question': q['question'],
                'correct_answer': q['correct'],
                'user_answer': user_answer,
                'is_correct': correct
            })
        return render(request, 'users/result.html', {'results': results})
    
    # Redirect to dashboard if accessed directly
    return redirect('dashboard')
