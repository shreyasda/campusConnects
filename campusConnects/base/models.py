from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    image = models.ImageField(null = True,blank = True, upload_to = 'media')
    title = models.CharField(max_length = 200)
    description = models.TextField()
    location = models.CharField(max_length = 200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    register_link = models.URLField(null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    def __str__(self):
        return self.title

class EventAnalytics(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
