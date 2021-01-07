from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.LoginView.as_view(), name='login_view'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrationView.as_view(), name='register')
]
