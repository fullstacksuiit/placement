from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about', about, name="about"),
    path('display', display_students, name="display"),
    path('registration', registration, name="registration"),
    path('contact', contact, name="contact"),
    path('signup', signup, name="signup"),
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path("edit/<str:rollno>", edit_info),
    path('gallery', gallery, name="gallery"),
    path("profile/<str:rollno>", profile, name="profile"),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)