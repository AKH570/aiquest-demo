# Generated by Django 4.1.7 on 2023-04-10 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('thana', models.CharField(max_length=50)),
                ('villorroad', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='Accepted', max_length=50)),
                ('Note', models.TextField(default=False, max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.courselist')),
                ('quantity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
