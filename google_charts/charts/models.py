from django.db import models
import math
from django.forms import forms
from django.conf import settings
from django.contrib.auth import settings


class Circle(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	radius=models.IntegerField()