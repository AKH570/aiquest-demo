from django.db import models
from django.contrib.auth.models import User

# Create your models here.

subject_expart =(
    ('Big Data Engineer','Big Data Engineer'),
    ('Data Analyst','Data Analyst'),
    ('Deep Learning for NLP & Computer Vision With Python','DL'),
    ('Python Django','Python Django'),)

class Expert(models.Model):
    name = models.CharField(max_length=100)
    sub_expart = models.CharField(choices=subject_expart,max_length=100)
    email = models.EmailField()
    profile_pic =models.ImageField(upload_to='expertimg')
    profile_details =models.TextField(max_length=300)
    date_of_joinig = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
class CourseList(models.Model):
    course_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount= models.FloatField()
    description = models.TextField(max_length=300)
    teachers =models.ForeignKey(Expert,on_delete=models.CASCADE)
    prod_img = models.ImageField(upload_to='courseimg')
    
    def __str__(self):
        return str(self.id)

class AboutPage(models.Model):
    title =models.CharField(max_length=200)
    descriptions=models.TextField(max_length=300)
    title_img=models.ImageField(upload_to='aboutimg')
    testmonial_text=models.TextField(max_length=200)
    testmonial_img=models.ImageField(upload_to='testmimg')
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(CourseList,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=100)
    villorroad = models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    location=models.CharField(max_length=300)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    subject=models.ForeignKey(CourseList,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.subject)
    
class ContactMsg(models.Model):
    name =models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    course_name =models.ForeignKey(Expert,on_delete=models.CASCADE)
    message=models.TextField(max_length=500)

    def __str__(self) -> str:
        return str(self.name)