from django.db import models

# Create your models here.
class Post(models.Model):
    user_id = models.IntegerField(max_length=10)
    title = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0,max_length=2)
