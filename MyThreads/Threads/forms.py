#Django forms are a powerful feature provided by Django to handle HTML forms, validate user input, and 
#process data securely and efficiently.They simplify the creation, validation, and rendering of forms in Django applications.
#Key Features of Django Forms:
#Form Field Definitions: You can define various types of fields like CharField, EmailField, IntegerField, etc.
#Validation: Django automatically validates the input for required fields, correct data types, and custom validation rules.
#HTML Form Rendering: Django can generate HTML forms dynamically from the form class.







from django import forms
from .models import mythread
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class threadform(forms.ModelForm):
    class Meta:
        model=mythread
        fields=['text','photo']


class userRegistrationForm(UserCreationForm):
    email =forms.EmailField()
    class Meta():
        model= User
        fields= ('username','email','password1','password2')  #Here we are giving tuple because we are using built-in model/forms of django
