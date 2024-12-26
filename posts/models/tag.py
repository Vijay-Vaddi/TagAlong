from django.db import models
from posts.models.post import Post

class Tag(models.Model):
    """Model for storing Tags for posts"""
    name = models.CharField(max_length=16)
    post = models.ManyToManyField(Post, blank=True, related_name='tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
