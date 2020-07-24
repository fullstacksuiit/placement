from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to="media/",null=True, blank=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone =  models.IntegerField(blank=True, null=True)
    dob = models.DateField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=20, null=True, blank=True)
    yearofcomp = models.CharField(max_length=50, blank=True, null=True)
    yearofadm = models.CharField(max_length=50, blank=True, null=True)
    rollno = models.CharField(max_length=20, null=True, blank=True, unique=True)
    course = models.CharField(max_length=50, blank=True, null=True)
    xth = models.FloatField(default=0.0)
    xthb = models.CharField(max_length=20, blank=True, null=True)
    xthp = models.IntegerField(blank=True, null=True)
    xii = models.FloatField(default=0.0)
    xiib = models.CharField(max_length=50, blank=True, null=True)
    xiip = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
         return self.rollno

class News(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to="media/",null=True, blank=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Signup(models.Model):
    password = models.CharField(max_length=50, blank=True, null=True)
    cnfpassword = models.CharField(max_length=50, blank=True, null=True)
    
class Event(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Placement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.student.rollno