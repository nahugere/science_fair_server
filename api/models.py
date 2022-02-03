from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ThreeDModel(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(null=False)
    # add a file field here
    more_info_link = models.CharField(max_length=500, blank=True, null=True, default="")
    more_info_text = models.CharField(max_length=20, blank=True, null=True, default="")
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
