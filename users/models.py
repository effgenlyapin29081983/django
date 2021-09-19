from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
import datetime


class User(AbstractUser):
    birthday = models.DateField(default=datetime.date(1970, 1, 1), blank=True, null=False)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + datetime.timedelta(minutes=20)))

    def safe_delete(self):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
