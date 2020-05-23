from django.contrib import admin
from .models import Profile


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_posted')


admin.site.register(Profile)


