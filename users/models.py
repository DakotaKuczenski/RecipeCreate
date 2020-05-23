from django.db import models
from django.contrib.auth.models import User
from recipes.models import Post
from PIL import Image
from django import forms
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    bio = models.TextField( max_length = 275)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


#    def save(self, *args, **kwargs):
#        super().save(*args, **kwargs)
#        img = Image.open(self.image.path)
#        if img.height > 300 or img.width > 300:
#            output_size = (300, 300)
#            img.thumbnail(output_size)
#            img.save(self.image.path)
