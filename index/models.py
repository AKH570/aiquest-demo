from django.db import models

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
        return self.name
class CourseList(models.Model):
    course_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount= models.FloatField()
    description = models.TextField(max_length=300)
    teachers =models.ForeignKey(Expert,on_delete=models.CASCADE)
    prod_img = models.ImageField(upload_to='courseimg')
    
    def __str__(self):
        return self.course_name