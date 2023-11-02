from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .models import SignUp


class GroupTasksForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))



class TaskForm(forms.Form):
    content = forms.CharField(max_length=200, label="ToDo Task")
    finish_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username", 
                               widget=forms.TextInput(attrs={"placeholder": "Username"}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
                               



class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
                               validators=[MinLengthValidator(6), MaxLengthValidator(18)])
    
    class Meta:
        model = SignUp
        fields = ("username", "email", "password")

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"})
        }
        
        