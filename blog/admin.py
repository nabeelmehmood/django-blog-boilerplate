from django.contrib import admin
from blog import models
# Register your models here.
admin.site.register(models.Comment)
admin.site.register(models.Post)