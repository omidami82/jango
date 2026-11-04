from django.shortcuts import render, get_object_or_404
from .models import Professor, Course
from django.views.generic import ListView, DetailView



def home(request):
    return render(request, 'computer/index.html')


def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'computer/professor_list.html', {'professors': professors})


def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    courses = professor.courses.all()
    return render(request, 'computer/professor_detail.html', {
        'professor': professor,
        'courses': courses,
    })


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'computer/course_detail.html', {'course': course})


def student(request):
    return render(request, 'computer/student.html')


def accountant(request):
    return render(request, 'computer/accountant.html')
# ... کدهای قبلی ...

class ProfessorListView(ListView):
    model = Professor
    template_name = 'computer/professor_list.html'
    context_object_name = 'professors'
    ordering = ['last_name']

class CourseListView(ListView):
    model = Course
    template_name = 'computer/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'computer/course_detail.html'
    context_object_name = 'course'