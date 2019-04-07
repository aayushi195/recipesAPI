# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mPassword = models.CharField(max_length=100)

    def __str__(self):
        return self.username;


class Recipe(models.Model):
    # Name field would not be null
    name = models.CharField(max_length=250, null=False)

    # One to one relationship between recipe and user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name;


class Step(models.Model):
    step_text = models.CharField(max_length=100,null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text;

class Ingredient(models.Model):
    ingredient_text = models.CharField(max_length=100,null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_text;


