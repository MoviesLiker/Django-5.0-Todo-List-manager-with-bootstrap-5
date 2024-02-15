from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user_id = models.ForeignKey(
        User, to_field="username", on_delete=models.CASCADE)
    task = models.TextField()
    date = models.TextField(default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
