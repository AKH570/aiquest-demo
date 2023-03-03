from django.urls import path
from home import views


urlpatterns = [
    path('ab/',views.about,name='about'),
    path('',views.index,name='index'),
]