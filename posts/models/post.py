from django.db import models
from users.models import User

class Post(models.Model):
    """Model for single event post by a user"""

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=False, blank=False)
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(max_length=256, blank=False, null=False)
    offer = models.CharField(max_length=256, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # reception

    class Meta:
        ordering = ['created_date_time']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

