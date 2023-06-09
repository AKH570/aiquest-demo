# Generated by Django 4.1.7 on 2023-04-15 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_contact_delete_orderplaced'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.expert')),
            ],
        ),
    ]
