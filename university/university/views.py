from django.shortcuts import render
from django.views.generic import ListView, DetailView
from computer.models import Professor, Course  # <--- این ایمپورت خیلی مهمه

def app_list(request):
    apps = [
        {
            'name': 'computer',
            'title': 'دانشکده کامپیوتر',
            'description': 'مدیریت دانشجویان، اساتید و دروس',
            'url_name': 'computer:home',
        },
        {
            'name': 'admin',
            'title': 'پنل ادمین',
            'description': 'مدیریت کامل دیتابیس از طریق جنگو ادمین',
            'url_name': None,
            'url_path': '/admin/',
        },
    ]
    return render(request, 'university/app_list.html', {'apps': apps})


# --- ویوهای Generic برای اساتید و دروس ---

class ProfessorListView(ListView):
    model = Professor
    template_name = 'university/professor_list.html'
    context_object_name = 'professors'
    ordering = ['last_name']

class CourseListView(ListView):
    model = Course
    template_name = 'university/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'university/course_detail.html'
    context_object_name = 'course'