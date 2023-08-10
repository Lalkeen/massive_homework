from django.db import models
from django.conf import settings

# Create your models here.


class BaseUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    bio = models.TextField(blank=True, null=True)
    prof_pic = models.ImageField(upload_to="images/%Y/%m/%d", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return "Profile for user {}".format(self.user.username)
