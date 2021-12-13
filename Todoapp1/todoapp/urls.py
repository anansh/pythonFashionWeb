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
from django.urls import path

from todolist.views import index
from todolist.views import mygym
from todolist.views import registerUser
from todolist.views import loadRegisteredUser
from todolist.views import deleteThisUser
from todolist.views import updateThisUser
from todolist.views import getThisUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', index, name="TodoList"),
    path('', mygym),
    path('registerUser/', registerUser),
    path('loadRegisteredUser/', loadRegisteredUser, name="UserList"),
    path('deleteThisUser/', deleteThisUser),
    path('updateThisUser/', updateThisUser),
    path('getRegisteredUser/', getThisUser)
]
