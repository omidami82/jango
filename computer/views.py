from django.shortcuts import render, get_object_or_404
from .models import Professor, Course


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