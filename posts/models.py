from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='posts/%y', default='no_picture.png')
    description = models.TextField()
    def __str__(self):
        return self.title
