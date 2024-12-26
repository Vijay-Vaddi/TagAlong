from django.db import models
from users.models import User

class Post(models.Model):
    """Model for single event post by a user"""
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(max_length=256, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    offer = models.CharField(max_length=256, null=True, blank=True)

    # reception 

    class Meta:
        ordering = ['created_date_time']


class PostDetails(models.Model):
    """Additional details for single event post"""
    type = (('Outdoor','Outdoor'),('Indoor','Indoor'))
    category = models.CharField(max_length=64,null=True, blank=True)
    out_or_in = models.CharField(max_length=32,choices=type)
    location_link = models.CharField(max_length=1000, null=True, blank=True)
    event_link = models.CharField(max_length=1000, null=True, blank=True)
