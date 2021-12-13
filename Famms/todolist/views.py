# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Todolist, Category
import datetime


# Create your views here.

def todoApp(request):  # the index view
    todos = Todolist.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager

    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = Todolist(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            # reloading the page

        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for todo_id in checkedlist:
                todo = Todolist.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo

    return render(request, "index.html", {"todos": todos, "categories": categories})


def index(request):
    return render(request, "index.html", {})


def product(request):
    return render(request, "product.html", {})


def blog(request):
    return render(request, "blog_list.html", {})


def contact(request):
    return render(request, "contact.html", {})
