from django import forms
from .models import PolicyRequest

class PolicyRequestForm(forms.ModelForm):
    class Meta:
        model = PolicyRequest
        fields = ['name', 'email', 'question']  # Only these fields should be editable by the user
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'question': forms.Textarea(attrs={'placeholder': 'Your Question or Clarification'}),
        }
