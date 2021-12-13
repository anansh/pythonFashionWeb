# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  # name to be shown when called


class Todolist(models.Model):  # Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created_time = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)  # a foreignkey

    class Meta:
        ordering = ["-created_time"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called


class Users(models.Model):  # Todolist able name that inherits models.Model
    name = models.TextField(max_length=250)
    email = models.TextField(max_length=250)
    mobile = models.TextField(max_length=250)
    message = models.TextField(max_length=250)

    class Meta:
        ordering = ["-name"]  # ordering by the name

    def __str__(self):
        return self.name  # name to be shown when called