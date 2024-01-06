from  django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change1'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('destinations', views.destinations, name='destinations')
]