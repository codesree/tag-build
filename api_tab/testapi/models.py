from django.db import models
from django import forms

class Reqarea(models.Model):
    #jsonreq = models.CharField(widget=forms.Textarea)
    API_request = models.TextField(max_length=5024*2)

class Resparea(models.Model):
    API_response = models.TextField(max_length=5024*2,)

