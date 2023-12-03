"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from dashboard.views import doctor_group_list, add_doctor_group, edit_doctor_group, add_user

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('login'), permanent=False), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('doctor-groups/', doctor_group_list, name='doctor_group_list'),
    path('doctor-groups/add/', add_doctor_group, name='add_doctor_group'),
    path('doctor-groups/<int:pk>/edit/', edit_doctor_group, name='edit_doctor_group'),
    path('add-user/', add_user, name='add_user'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]

