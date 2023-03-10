from django.db import models


# Create your models here.
subject_expart =(
    ('BD','Big Data Engineer'),
    ('DA','Data Analyst'),
    ('DL','Deep Learning for NLP & Computer Vision With Python'),)

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    sub_expart = models.CharField(choices=subject_expart,max_length=100)
    email = models.EmailField()
    profile_pic =models.ImageField(upload_to='teachersimg')
    date_of_joinig = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


