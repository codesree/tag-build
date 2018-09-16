from djongo import models
from django import forms
from django.contrib.auth.models import User

class tag_check(models.Model):
    #jsonreq = models.CharField(widget=forms.Textarea)
    tag_id = models.CharField(max_length=234,unique=True)

    def __str__(self):
        return self.tag_id


class Userpro(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username









