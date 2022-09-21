from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user
