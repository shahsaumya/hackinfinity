from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.models import model_to_dict
# Create your models here.


class MyUser(AbstractUser):
    mobile_no = models.CharField(max_length=10, unique=True)
    user_type = models.NullBooleanField(null=True)


class State_translator(models.Model):
    state_name = models.CharField(max_length=50, default=None)
    state_language = models.CharField(max_length=50, default=None)
    state_code = models.CharField(max_length=20, default="en")

    def __str__(self):
        return self.state_name

    def to_dict(self):
        return model_to_dict(self)


class Produce(models.Model):
    user = models.ForeignKey('MyUser')
    crop = models.CharField(max_length=30)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10)


class Support(models.Model):
    user = models.ForeignKey("MyUser")
    support_text = models.TextField()
    is_read = models.BooleanField()

    def __init__(self, user, support_text, is_read=False):
        self.user = user
        self.is_read = is_read
        self.support_text = support_text


class Feedback(models.Model):
    user_id = models.ForeignKey('MyUser')
    aadhar = models.CharField(max_length=16)
    feedback = models.CharField(max_length=1000)