from django import forms

class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=45) 
    email = forms.EmailField()

class DemoForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField()

class VolunteerForm(forms.Form):
    fullName = forms.CharField(max_length=40)
    email = forms.EmailField()
    role = forms.CharField(max_length=20)