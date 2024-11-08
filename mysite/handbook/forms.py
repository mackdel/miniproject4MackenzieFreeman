from django import forms
from .models import PolicyRequest

class PolicyRequestForm(forms.ModelForm):
    class Meta:
        model = PolicyRequest
        fields = ['name', 'email', 'question']  # Only these fields should be editable by the user
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100','placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control w-100','placeholder': 'Your Email','required': 'required'}),
            'question': forms.Textarea(attrs={'class': 'form-control w-100','placeholder': 'Your Question or Clarification','required': 'required'}),
        }
