'''from .forms import Customer
from django.forms import ModelForm

class custumerClass(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'''
        
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'First_name': 'First Name',
            'Last_name': 'Last Name',
            'phone': 'Phone Number',
            'Email': 'Email Address',
            'birth_date': 'Date of Birth',
            'membership': 'Membership Type',
            'points': 'Reward Points',
            'password': 'Password',
        }
        error_messages = {
            'First_name': {
                'max_length': 'First name cannot exceed 200 characters.',
                'required': 'Please enter your first name.',
            },
            'Last_name': {
                'max_length': 'Last name cannot exceed 200 characters.',
                'required': 'Please enter your last name.',
            },
            'phone': {
                'max_length': 'Phone number cannot exceed 255 characters.',
                'required': 'Please enter your phone number.',
            },
            'Email': {
                'invalid': 'Enter a valid email address.',
                'required': 'Please enter your email address.',
            },
            'birth_date': {
                'invalid': 'Enter a valid date of birth.',
            },
             'password': {
                'required': 'Please enter a password.',
            }
        }
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Select your birth date', 'type': 'text'}),
            'membership': forms.Select(attrs={'class': 'form-control'}),
            'points': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter reward points'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
