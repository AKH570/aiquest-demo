from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from courses import views


urlpatterns = [
    path('sq/',views.courses,name='sqldata'),
    path('ml/',views.dataml,name='dsml'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)