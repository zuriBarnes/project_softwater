from django import forms

class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=45) 
    email = forms.EmailField()

class DemoForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField()