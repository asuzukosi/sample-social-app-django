from urllib import request
from django.shortcuts import render
from django.views.generic import FormView
from social_media.apps.authentication.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SettingsForm
from authentication.models import Profile

# Create your views here.
class SignUpView(FormView):
    form_class = SignUpForm
    success_url = "/login/"
    template_name = "signup.html"

    def form_invalid(self, form: SignUpForm):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def form_valid(self, form: SignUpForm):
        form.create_user()
        return super().form_valid(form)


class AccountSettings(LoginRequiredMixin, FormView):
    template_name = "setting.html"
    form_class = SettingsForm
    success_url = "/settings/"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        data["profile_image"] = profile.profile_image
        data["profile"] = profile
        return data

    def form_valid(self, form: SignUpForm):
        print(form.cleaned_data)
        Profile.objects.filter(user=self.request.user).update(
            location=form.cleaned_data["location"], bio=form.cleaned_data["bio"]
        )
        profile: Profile = Profile.objects.get(user=self.request.user)
        if form.cleaned_data["image"]:
            profile.profile_image = form.cleaned_data["image"]
            profile.save()

        return super(AccountSettings, self).form_valid(form)
