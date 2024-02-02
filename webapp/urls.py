from django.urls import path
from . import views 
from .views import create_student, get_student_data, update_student, create_course



urlpatterns = [
    path('', views.home_page, name="index"),
    path('about/', views.about_page, name="about"),
    path('login/', views.login_page, name="login"),
    path('home/', views.home_page, name="home"),  # Add this line
    path('subjects/', views.subjects_view, name='subjects'),
    path('grade/', views.grade_view, name='grade'),
    path('faculty/', views.faculty_view, name='faculty'),
    path('department/', views.department_view, name='department'),
    path('students/', views.student_view, name='student'),
    path('room/', views.room_view, name='room'),
    path('class/', views.class_view, name='class'),
    path('users/', views.users_view, name='users'),
    path('students/create/', create_student, name='create_student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    #path('course/create/', create_student, name='create_student'),
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/create/', create_course, name='create_course'),
    path('update_course/<int:pk>/', views.update_course, name='update_course'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),
   
]
