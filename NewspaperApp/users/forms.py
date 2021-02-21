# COMBAK: users/forms.py

# Update Two Django forms: UserCreationForm and UserChangeForm (for superuser)

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Import our CustomUser from models.py
from .models import CustomUser

# Make new updated classes

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
