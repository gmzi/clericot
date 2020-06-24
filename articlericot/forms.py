from django import forms
from django.forms import URLField


class ArticleLink(forms.Form):
    article_url = forms.URLField()