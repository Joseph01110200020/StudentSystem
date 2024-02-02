from django.contrib import admin

# Register your models here.

from .models import Student, Course, Enrollment, Grade
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)