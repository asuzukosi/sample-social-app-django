from datetime import datetime
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from social_media.apps.feed.forms import CommentForm, PostForm
from feed.models import Post, Comment

# Create your views here.
class FeedListPage(LoginRequiredMixin, ListView):
    template_name = "home.html"
    model = Post
    context_object_name = "posts"


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


@login_required()
def upload_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if not form.is_valid():
            return redirect(request.META["HTTP_REFERER"], permanent=True)
        post = Post.objects.create(owner=request.user, image=request.FILES['image'], **form.cleaned_data)
    return redirect(request.META["HTTP_REFERER"], permanent=True)


@login_required()
def upload_comment(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=id)
        print(request.POST)
        form = CommentForm(request.POST)
        if not form.is_valid():
            return redirect(request.META["HTTP_REFERER"], permanent=True)
        comment = Comment.objects.create(user=request.user, post=post, **form.cleaned_data)
    return redirect(request.META["HTTP_REFERER"], permanent=True)
