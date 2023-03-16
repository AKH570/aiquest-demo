from django.urls import path
from index import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as login_views
from . form import LoginForm


urlpatterns = [
    path('',views.CourseView.as_view(),name='index'),
    path('regi/',views.RegistrationView.as_view(),name='registration'),
    path('djai/',views.DjwebaiVie.as_view(),name='djwebai'),
    path('bigd/',views.BigDataView.as_view(),name='bigdata'),
    path('dlnl/',views.DeepLearningView.as_view(),name='dlnlp'),
    path('dana/',views.DataAnalystView.as_view(),name='dataanalyst'),
    path('dsml/',views.DataMLView.as_view(),name='datascml'),
    path('sqld/',views.SqlDsView.as_view(),name='sqldatasc'),
    path('abus/',views.AboutView.as_view(),name='about'),
    path('accounts/login/',login_views.LoginView.as_view(template_name='index/login.html',authentication_form=LoginForm),name='login')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)