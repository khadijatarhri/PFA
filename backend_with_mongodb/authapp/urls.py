from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.RegisterView.as_view(), name='api-register'),
    path('api/login/', views.LoginView.as_view(), name='api-login'),
    path('api/home/', views.HomeView.as_view(), name='api-home'),

    # Vues HTML
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home_page, name='home'),
]
