from django.db import models
from users.models import User
from posts.models.post import Post

class PostDetails(models.Model):
    """Additional details for single event post"""
    outdoor_or_indoor_choices = (
        ('Outdoor','Outdoor'),
        ('Indoor','Indoor')
        )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    category = models.CharField(max_length=64,null=True, blank=True)
    outdoor_or_indoor = models.CharField(max_length=32, choices=type)
    location_link = models.CharField(max_length=1000, null=True, blank=True)
    event_link = models.CharField(max_length=1000, null=True, blank=True)
