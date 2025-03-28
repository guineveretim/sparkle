from django.urls import path

from marasparkle.forms import ResetPasswordConfirmForm, ResetPasswordForm
from . import views
from django.contrib.auth import views as auth_views
from .views import create_booking, booking_success



urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about_view, name='about'),
    path('services/',views.Service,name='services_details'),
    path('login/', views.login_view, name= 'login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
 

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html',
        form_class=ResetPasswordForm
    ), name='password_reset'),

    
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html'
    ), name='password_reset_done'),

    
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html',
        form_class=ResetPasswordConfirmForm
    ), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html'
    ), name='password_reset_complete'),
    
     
      path('booking/', create_booking, name='create_booking'),
    path('booking-success/<int:booking_id>/', booking_success, name='booking_success'),


    
]
