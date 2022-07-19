from django.forms import Form
from django import forms
from django.contrib.auth import get_user_model
from authentication.models import Profile


class SignUpForm(Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean(self):
        super(SignUpForm, self).clean()
        if (
            "password" not in self.cleaned_data
            or "confirm_password" not in self.cleaned_data
        ):
            raise forms.ValidationError("Password and Confirm Password are required")
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        if get_user_model().objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("Email already exists")
        if (
            get_user_model()
            .objects.filter(username=self.cleaned_data["username"])
            .exists()
        ):
            raise forms.ValidationError("Username already exists")

    def create_user(self):
        del self.cleaned_data["confirm_password"]
        user = get_user_model().objects.create_user(**self.cleaned_data)
        Profile.objects.create(user=user)
        return user


class SettingsForm(forms.Form):
    image = forms.ImageField()
    bio = forms.CharField()
    location = forms.CharField()
