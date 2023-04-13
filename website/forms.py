from django import forms
from django.forms import ModelForm
from .models import Sub

class DemoForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField()

class VolunteerForm(forms.Form):
    fullName = forms.CharField(max_length=40)
    email = forms.EmailField()
    role = forms.CharField(max_length=20)


class SubscribeForm(ModelForm):
    class Meta:
        model = Sub
        fields = ['full_name', 'email']