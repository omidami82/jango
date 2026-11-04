from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # هدایت آدرس /computer/ به اپ کامپیوتر
    path('computer/', include('computer.urls')), 
]