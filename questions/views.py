from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Question
import random


@login_required
def home(request):
    return render(request, 'questions/home.html')


@login_required
def add_question(request):
    if request.method == 'POST':
        Question.objects.create(
            department=request.POST['department'],
            subject=request.POST['subject'],
            unit=request.POST['unit'],
            difficulty=request.POST['difficulty'],
            marks=request.POST['marks'],
            question_text=request.POST['question_text']
        )
        return redirect('view_questions')

    return render(request, 'questions/add_question.html')


@login_required
def view_questions(request):
    questions = Question.objects.all().order_by('-created_at')

    return render(
        request,
        'questions/view_questions.html',
        {'questions': questions}
    )


@login_required
def generate_question_paper(request):

    questions = []

    if request.method == 'POST':

        department = request.POST.get('department')
        subject = request.POST.get('subject')
        unit = request.POST.get('unit')
        difficulty = request.POST.get('difficulty')
        marks = request.POST.get('marks')

        matching_questions = Question.objects.filter(
            department=department,
            subject=subject,
            unit=unit,
            difficulty=difficulty,
            marks=marks
        )

        matching_questions = list(matching_questions)

        random.shuffle(matching_questions)

        questions = matching_questions[:5]

    return render(
        request,
        'questions/generate_question_paper.html',
        {
            'questions': questions
        }
    )

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(
            request,
            'questions/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'questions/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def delete_question(request, question_id):

    question = get_object_or_404(Question, id=question_id)

    question.delete()

    return redirect('view_questions')
@login_required
def edit_question(request, question_id):

    question = get_object_or_404(
        Question,
        id=question_id
    )

    if request.method == 'POST':

        question.department = request.POST['department']
        question.subject = request.POST['subject']
        question.unit = request.POST['unit']
        question.difficulty = request.POST['difficulty']
        question.marks = request.POST['marks']
        question.question_text = request.POST['question_text']

        question.save()

        return redirect('view_questions')

    return render(
        request,
        'questions/edit_question.html',
        {'question': question}
    )