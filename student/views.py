from django.shortcuts import redirect, render
from .models import *
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    today = datetime.now()
    events = Event.objects.filter(date__gte=today).order_by('date')
    news = News.objects.all().order_by('date')
    context = {"events": events, "news": news}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def display_students(request):
    year = 2020
    students = Student.objects.filter(yearofcomp=year)
    if request.method == "POST":
        rp = request.POST
        year = rp.get("year")
        students = Student.objects.filter(yearofcomp=year)
        course = rp.get("course")
        if course is not None:
            students = students.objects.filter(course=course)
        branch = rp.get("branch")
        if branch is not None:
            students = students.objects.filter(branch=branch)
    students = students.order_by('rollno')
    context = {"students": students, 'year': year}
    return render(request, 'display.html', context)
    
def contact(request):
    return render(request, 'contact.html')
# def students(request):
#     students = Student.objects.all()
#     placed = Placement.objects.all()
#     context = {"students": students, "placed": placed}
#     return render(request, 'student.html', context)

def registration(request):
    if request.method == "POST":
        rollno = request.POST.get("rollno").upper()
        if Student.objects.filter(rollno=rollno).exists():
                context = {"error" : "Already Registered"}
                return render(request, 'registration.html', context=context)
        image = request.FILES.get("image")
        fullname = request.POST.get("fullname").upper()
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        branch = request.POST.get("branch")
        yearofcomp = request.POST.get("yearofcomp")
        yearofadm = request.POST.get("yearofadm")
        course = request.POST.get("course")
        xth = request.POST.get("xth")
        xthb = request.POST.get("xthb")
        xthp = request.POST.get("xthp")
        xii = request.POST.get("xii")
        xiib = request.POST.get("xiib")
        xiip = request.POST.get("xiip")
        stud = Student(image=image, fullname=fullname, gender=gender, email=email, dob=dob, phone=phone, branch=branch, yearofcomp=yearofcomp, yearofadm=yearofadm, rollno=rollno, course=course, xth=xth, xthb=xthb, xthp=xthp, xii =xii, xiib =xiib, xiip = xiip)
        stud.save()
        context = {"roll": rollno}
        return render(request, "signup.html", context)

    return render(request, "registration.html")


def signup(request):
    if request.method == "POST":
        rollno = request.POST.get("rollno")
        password = request.POST.get("password")
        cnfpassword = request.POST.get("cnfpassword")
        if password!=cnfpassword:
            context = {"message": "Password not Matched", "roll": rollno}
            return render(request, 'signup.html', context=context)
        encrypted_password = make_password(password)
        stud = Student.objects.get(rollno=rollno)
        user = User(username=rollno, password=encrypted_password, email=stud.email)
        user.save()
        # * return login page.
        return redirect("login")
    return render(request, "signup.html")


def login_user(request):
    if request.method == "POST":
        rollno = request.POST.get("rollno")
        password = request.POST.get("password")
        user = authenticate(request, username=rollno, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

@login_required
def student(request, rollno):
    student = Student.objects.get(rollno=rollno)
    context = {"student": student}
    return render(request, "profile.html", context)

@login_required
def profile(request):
    rollno = request.user.username
    return student(request, rollno)
    
def gallery(request):
    photos = Gallery.objects.all()
    context = {"photos": photos}
    return render(request, "gallery.html", context)

def news_display(request):
    display = News.objects.all()
    event_info = Event.objects.all()
    context = {"news": display, "event": event_info}
    return render(request, 'new.html', context)

def event_display(request):
    today = datetime.now()
    events = Event.objects.filter(date__gte=today)
    context = {"events": events}
    return render(request, "event.html", context)

@login_required
def edit_info(request, rollno):
    # POST request
    if request.method == "POST":
        image = request.FILES.get("image")
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        branch = request.POST.get("branch")
        yearofcomp = request.POST.get("yearofcomp")
        yearofadm = request.POST.get("yearofadm")
        course = request.POST.get("course")
        xth = request.POST.get("xth")
        xthb = request.POST.get("xthb")
        xthp = request.POST.get("xthp")
        xii = request.POST.get("xii")
        xiib = request.POST.get("xiib")
        xiip = request.POST.get("xiip")
        Student.objects.filter(rollno=rollno).update(fullname=fullname, gender=gender, email=email, dob=dob, phone=phone, branch=branch, yearofcomp=yearofcomp, yearofadm=yearofadm, course=course, xth=xth, xthb=xthb, xthp=xthp, xii=xii, xiib=xiib, xiip=xiip)
    student = Student.objects.get(rollno=rollno)
    context = {"student": student}
    return render(request, "edit-profile.html", context)

@login_required
def logout_user(request):
    logout(request)
    return redirect("login")