# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Todolist, Category, Users


# Create your views here.

def index(request):  # the index view
    todos = Todolist.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager

    if request.method == "POST":  # checking if the request method is a POST
        pass
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            todo = Todolist(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            todo.save()  # saving the todo
            return redirect("/")  # reloading the page

        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checklist = request.POST["checkbox"]  # checked todos to be deleted
            for todo_id in checklist:
                todo = Todolist.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo

    return render(request, "index.html", {"todos": todos, "categories": categories})


def mygym(request):
    registeredUsers = Users.objects.count()
    return render(request, "index.html", {"registeredUsers": registeredUsers})


def registerUser(request):
    res = {}
    print(request)
    data = json.loads(request.POST.get('data', ''))[0]
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in data["taskAdd"]:  # checking if there is a request to add a todo
            name = data["name"]
            email = data["email"]
            mobile = data["mobile"]
            message = data["message"]
            inquiry = Users(name=name, email=email, mobile=mobile, message=message)
            temp = inquiry.save()
            registeredUsers = Users.objects.count()
            res = {'response': 'Success', 'message': 'Member registered successfully',
                   'registeredUsersCount': registeredUsers}
            return JsonResponse(res)


def loadRegisteredUser(request):
    registeredUsers = Users.objects.all()
    test = serializers.serialize("json", registeredUsers)
    res = {'response': 'Success', 'message': 'All members loaded successfully',
           'users': test}
    return JsonResponse(res)


def deleteThisUser(request):
    pk = json.loads(request.POST.get('data', ''))[0]["pk"]
    userData = Users.objects.get(id=int(pk))  # getting todo id
    userData.delete()
    registeredUsers = Users.objects.count()
    res = {'response': 'Success', 'message': 'Member deleted successfully', 'registeredUsersCount': registeredUsers}
    return JsonResponse(res)


def getThisUser(request):
    pk = json.loads(request.POST.get('data', ''))[0]["pk"]
    userData = Users.objects.filter(id=int(pk))  # getting todo id
    test = serializers.serialize("json", userData)
    res = {'response': 'Success', 'message': 'Member deleted successfully', 'userData': test}
    return JsonResponse(res)


def updateThisUser(request):
    data = json.loads(request.POST.get('data', ''))[0]
    name = data["name"]
    email = data["email"]
    mobile = data["mobile"]
    message = data["message"]
    pk = data["pk"]
    Users.objects.filter(id=int(pk)).update(name=name, email=email, mobile=mobile, message=message)
    res = {'response': 'Success', 'message': 'Member updated successfully'}
    return JsonResponse(res)
