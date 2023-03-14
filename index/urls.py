from django.urls import path
from index import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . form import LoginForm


urlpatterns = [
    #path('ab/',views.about,name='about'),
    #path('',views.index,name='index'),
    path('',views.CourseView.as_view(),name='index'),
    path('regi/',views.RegistrationView.as_view(),name='registration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='index/login.html',authentication_form=LoginForm),name='login')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)