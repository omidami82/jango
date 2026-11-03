from django.shortcuts import render


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

#class ProfessorListView(ListView):
 #   model = Professor
  #  template_name = 'university/professor_list.html'  # اسم و مسیر قالب
   # context_object_name = 'professors'                 # اسم متغیری که در قالب استفاده می‌کنیم
    #ordering = ['last_name']   
                            # مرتب‌سازی بر اساس فامیل