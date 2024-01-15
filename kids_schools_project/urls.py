"""
URL configuration for kids_schools_project project.

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
from django.contrib import admin
from django.urls import path
from authentication_src.views import inscription_form, login_user, home, logout_user, get_users, update_user, delete_user
from kids_schools_management.views import create_school, get_schools, update_school, delete_school


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription_form/', inscription_form, name='inscription-form'),
    path('login_user/', login_user, name='login-user'),
    path('home/', home, name='home'),
    path('logout_user/', logout_user, name='logout-user'),
    path('get_users/', get_users, name='get-users'),
    path('update_user/<int:id>/modify', update_user, name='update-user'),
    path('delete_user/<int:id>/delete', delete_user, name='delete-user'),
    path('create_school/', create_school, name='create-school'),
    path('get_schools/', get_schools, name='get-schools'),
    path('update_school/<int:id>/modify', update_school, name='update-school'),
    path('delete_school/<int:id>/delete', delete_school, name='delete-school'),
]
