"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.SignupPage, name = 'signup'),
    path('login/', views.LoginPage, name = 'login'),
    path('home/', views.HomePage, name = 'home'),
    path('logout/', views.LogoutPage, name = 'logout'),
    path('profile/', views.ProfilePage, name = 'profile'),
    path('adminn/', views.AdminnPage, name = 'adminn'),
    path('approve/', views.ApprovePage, name = 'approve'),
    path('create_product/', views.CreateProductPage, name = 'create_product'),
    path('user_list/', views.UsersPage, name = 'user_list'),
    path('edit_profile/', views.EditProfilePage, name = 'edit_profile'),
    path('search/', views.SearchPage, name = 'search'),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
