from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)

    projects = models.ManyToManyField("LargeProject", related_name="projects", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class LargeProject(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    date_created = models.CharField(max_length=200,null=True)
    due_date = models.CharField(max_length=200,null=True)

    sub_projects = models.ManyToManyField("SubProject", related_name="sub_projects", blank=True)


class SubProject(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    documents = models.ManyToManyField("Document", related_name="documents", blank=True)
    ideations = models.ManyToManyField("Ideation", related_name="ideation", blank=True)
    

class Document(models.Model):
    name = models.CharField(max_length=200,null=True)
    number = models.CharField(max_length=200,null=True)
    due_date = models.CharField(max_length=200,null=True)
    doc_type = models.CharField(max_length=200,null=True)  # essay or ideation
    prompt = models.CharField(max_length=500,null=True)
    content = models.CharField(max_length=500,null=True)

class Ideation(models.Model):  
    name = models.CharField(max_length=200,null=True)
    nodesAndLinks = models.JSONField(default=dict)  
    prompt = models.CharField(max_length=500,null=True)



class ToDoItem(models.Model):
    description = models.CharField(max_length=200,null=True)
    completed = models.BooleanField(null=True, blank=True)
