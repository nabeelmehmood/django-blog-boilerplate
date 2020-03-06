from django.contrib import admin
from blog import models

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.Comment)
admin.site.register(models.Post)
admin.site.register(models.Category)
