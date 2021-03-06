"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from todolist.views import todoApp
from todolist.views import index
from todolist.views import product
from todolist.views import blog
from todolist.views import contact
from todolist.views import about
from todolist.views import testimonial
from todolist.views import login
from todolist.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('todolist/', todoApp, name="TodoList"),
    path('', index),
    path('product/', product),
    path('blog/', blog),
    path('contact/', contact),
    path('about/', about),
    path('testimonial/', testimonial),
    path('signIn/', login),
    path('register/', register)
]
