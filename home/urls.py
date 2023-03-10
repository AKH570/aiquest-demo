from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views


urlpatterns = [
    path('ab/',views.about,name='about'),
    path('',views.ProductView.as_view(),name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)