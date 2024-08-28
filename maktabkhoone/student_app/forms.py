from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signup_form(UserCreationForm) :
    email = forms.EmailField(required= True)

    class meta :
        model = User
        fields = ['name' , 'email' , "phone_number"]
    