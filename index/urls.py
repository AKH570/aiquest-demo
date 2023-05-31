from django.urls import path
from index import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . form import LoginForm


urlpatterns = [
    path('',views.CourseView.as_view(),name='index'),
    path('regi/',views.RegistrationView.as_view(),name='registration'),
    path('codt/<int:pk>',views.CourseDetailPage.as_view(),name='coursedetails'),
    path('djai/',views.DjwebaiVie.as_view(),name='djwebai'),
    path('bigd/',views.BigDataView.as_view(),name='bigdata'),
    path('dlnl/',views.DeepLearningView.as_view(),name='dlnlp'),
    path('dana/',views.DataAnalystView.as_view(),name='dataanalyst'),
    path('dsml/',views.DataMLView.as_view(),name='datascml'),
    path('sqld/',views.SqlDsView.as_view(),name='sqldatasc'),
    path('abus/',views.AboutView.as_view(),name='about'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='index/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page ='login'),name='logout'),
    path('add-to-cart/',views.AddtoCart,name='addtocart'),
    path('cart/',views.Info_Cart,name='infocart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('checkout/',views.checkout,name='checkout'),
    path('address/',views.AddressView.as_view(),name='address'),
    path('paymentdone/',views.payment,name='pament'),
    #path('contact/',views.contact,name='contact'),
    path('contact/',views.ContactUs.as_view(),name='contact'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)