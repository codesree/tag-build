from django import forms
from .models import Resparea,Reqarea

class Reqform(forms.ModelForm):
    class Meta:
        model = Reqarea
        fields = '__all__'


class Respform(forms.ModelForm):
    class Meta:
        model = Resparea
        fields = '__all__'
