from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class BolgArticles(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,related_name="bolg_posts",on_delete=models.CASCADE)
    body = models.TextField()
    publish=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=("-publish",)
    def __str__(self):
        return  self.title