from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    """
    Profile mapped to a user to store
    additional information.
    """

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()
    profile_image = models.ImageField(
        upload_to="profile_image", default="blank-profile-picture.png"
    )
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
