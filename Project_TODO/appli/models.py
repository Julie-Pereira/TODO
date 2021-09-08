from django.db import models

class Todo(models.Model):
    title = models.TextField(null=True)
    states = models.TextField(null=True)