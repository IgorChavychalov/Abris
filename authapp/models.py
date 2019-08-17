from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from datetime import timedelta


# def activation_key_expired():
#     return now() + timedelta(hours=48)

# Create your models here.
class User(AbstractUser):
    pass
    # # активация по e-mail
    # activation_key_expires = models.DateTimeField(default=activation_key_expired)
    #
    # def is_activation_key_valid(self):
    #     return now() <= self.activation_key_expires
