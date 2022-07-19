from django import forms


class PostForm(forms.Form):
    caption = forms.CharField()


class CommentForm(forms.Form):
    comment = forms.CharField()
