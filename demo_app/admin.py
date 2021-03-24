from django.contrib import admin

# Register your models here.
from demo_app import models

admin.site.register(models.UserProfile)
