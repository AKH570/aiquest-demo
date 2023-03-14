# Generated by Django 4.1.7 on 2023-03-12 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub_expart', models.CharField(choices=[('Big Data Engineer', 'Big Data Engineer'), ('Data Analyst', 'Data Analyst'), ('Deep Learning for NLP & Computer Vision With Python', 'DL'), ('Python Django', 'Python Django')], max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(upload_to='expertimg')),
                ('profile_details', models.TextField(max_length=300)),
                ('date_of_joinig', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('description', models.TextField(max_length=300)),
                ('prod_img', models.ImageField(upload_to='courseimg')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.expert')),
            ],
        ),
    ]
