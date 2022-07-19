from django.urls import path
from .views import FeedListPage, upload_comment, upload_post

app_name = "feed"
urlpatterns = [
    path("", FeedListPage.as_view(), name="home"),
    path("upload", upload_post, name="upload_post"),
    path("upload_comment/<int:id>/", upload_comment, name="upload_comment"),
]
