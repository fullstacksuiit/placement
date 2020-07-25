from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from student.views import *

urlpatterns = [
    path('user/admin/', admin.site.urls),
    path('', index, name="index"),
    path('about', about, name="about"),
    path('students', display_students, name="students"),
    path('register', registration, name="register"),
    path('contact', contact, name="contact"),
    path('signup', signup, name="signup"),
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path("edit/<str:rollno>", edit_info, name="edit"),
    path('gallery', gallery, name="gallery"),
    path("profile", profile, name="profile"),
    path("student/<str:rollno>", student, name="student"),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SUIIT Admin'
                