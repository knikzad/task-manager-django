from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
  STATUS_CHOICES = [
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
  ]
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  title = models.CharField(max_length = 200)
  description = models.TextField()
  due_date = models.DateField()
  status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'in_progress')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)