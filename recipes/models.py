from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from multiselectfield import MultiSelectField
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=75)
    Ingredients = models.CharField(max_length=500)
    Steps = models.TextField()
    Additional = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    recipe_image = models.ImageField(default="default.jpg", upload_to='recipe_pics')
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    follow = models.ManyToManyField(User, related_name='follow', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    DIET_CHOICES= (
    ('raw', 'Raw'),
    ('vegan', 'Vegan'),
    ('vegetarian', 'Vegetarian'),
    ('other', 'Other'),
    )

    Diet= MultiSelectField(choices = DIET_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    #added this meta class for dynamic
    class meta:
        db_table = 'ingredient'
