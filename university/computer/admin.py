from django.contrib import admin
from .models import Student, Professor, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email')
    search_fields = ('first_name', 'last_name', 'student_id')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code', 'department')
    search_fields = ('first_name', 'last_name', 'department')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'units', 'professor')
    search_fields = ('title', 'code')
    list_filter = ('professor', 'units')
    filter_horizontal = ('students',)