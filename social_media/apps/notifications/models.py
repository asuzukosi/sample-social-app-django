from django.db import models

# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=255)
    # reference_post = models.ForeignKey("Post")
    # reference_user = models.ForeignKey("User")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
