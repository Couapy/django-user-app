from django import forms
from django.contrib.auth.models import User
from .models import Profile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "biography",
            "website",
            "avatar",
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
