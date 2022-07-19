from .views import AccountSettings, SignUpView
from django.urls import path

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("settings/", AccountSettings.as_view(), name="settings"),
]
