from django import forms
from .models import *


class CommentCreateForm(forms.ModelForm):
    """Форма комментариев"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
