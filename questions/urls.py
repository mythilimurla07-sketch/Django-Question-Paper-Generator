from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('add-question/', views.add_question, name='add_question'),

    path('view-questions/', views.view_questions, name='view_questions'),

    path(
        'generate-question-paper/',
        views.generate_question_paper,
        name='generate_question_paper'
    ),
    path(
    'delete-question/<int:question_id>/',
    views.delete_question,
    name='delete_question'
),

path(
    'edit-question/<int:question_id>/',
    views.edit_question,
    name='edit_question'
),
]