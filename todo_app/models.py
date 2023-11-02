from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class SignUp(User):
    pass


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    content = models.TextField(max_length=1000)
    finish_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)
    date_reached = models.BooleanField(default=False)
    

class ConnectedUsers(models.Model):
    user_id = models.CharField(max_length=100000)
    user_channel = models.CharField(max_length=100000)



