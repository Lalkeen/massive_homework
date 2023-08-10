from django.contrib import admin
from .models import BaseUser

# Register your models here.


class BaseUserAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "prof_pic"]


admin.site.register(BaseUser, BaseUserAdmin)
