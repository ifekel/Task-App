from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    favorite = models.BooleanField(default=False, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title