
from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from .models import *
from .models import Student
from .models import Course
from .forms import StudentForm
from .forms import CourseForm

# Create your views here.
def home_page(request):
    students = Student.objects.all()
    return render(request, 'pages/home.html', {'students': students})

def about_page(request):
    return render(request, 'pages/about.html')

def login_page(request):
    return render(request, 'pages/login.html')

def subjects_view(request):
    courses = Course.objects.all()
    return render(request, 'pages/subjects.html', {'courses': courses})

def grade_view(request):
    return render(request, 'pages/grade.html')

def faculty_view(request):
    students = Student.objects.all()
    return render(request, 'pages/faculty.html', {'students': students})

def department_view(request):
    return render(request, 'pages/department.html')

def student_view(request):
   students = Student.objects.all()
   return render(request, 'pages/student.html', {'students': students})


def room_view(request):
    return render(request, 'pages/room.html')

def class_view(request):
    return render(request, 'pages/class.html')

def users_view(request):
    return render(request, 'pages/users.html')

#Create student_details view
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    context = {
        'form': StudentForm()
    }
    return render(request, 'pages/student.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'subject.html', {'courses': courses})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page

    context = {
        'form': form
    }
   
    return render(request, 'pages/update_student.html', context)

#Create delete_student view
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
     student.delete()
     return redirect('/')  # Redirect to a success page
    
    context = {
        'form': student
    }
   
    return render(request, 'pages/delete_student.html', context)


#Create get_student_data view
def get_student_data(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    data = {
        'first_name': student.first_name,
        'last_name': student.last_name,
        'email': student.email
    }
    return JsonResponse(data)


def subjects(request):
    courses = CourseForm.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'pages/subjects.html', context)

#Create get_student_data view
def get_course_data(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    data = {
        'course_name': course.course_name,
    }
    return JsonResponse(data)

#Create course_details view
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    context = {
        'form': CourseForm()
    }
    return render(request, 'pages/subjects.html', context)


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page

    context = {
        'form': form
    }
   
    return render(request, 'pages/update_course.html', context)



def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
     course.delete()
     return redirect('/')  # Redirect to a success page
    
    context = {
        'form': course
    }
   
    return render(request, 'pages/delete_course.html', context)


def showthis(request):
    count = Student.objects.count()  # count the number of students
    context= {'count': count}
    return render(request, 'pages/home.html', context)