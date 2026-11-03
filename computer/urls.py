from django.urls import path
from . import views

app_name = 'computer'

urlpatterns = [
    path('', views.home, name='home'),
    path('professors/', views.professor_list, name='professor_list'),
    path('professors/<int:pk>/', views.professor_detail, name='professor_detail'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('student/', views.student, name='student'),
  #  path('accountant/', views.accountant, name='accountant'),
]