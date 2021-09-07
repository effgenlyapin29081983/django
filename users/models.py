from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    birthday = models.DateField(default=datetime.date(1970, 1, 1), blank=True, null=False)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    def safe_delete(self):
        self.is_active = False
        self.save()