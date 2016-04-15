from django import forms
from .models import Bookmark
import re


class CreateBookmarkForm(forms.ModelForm):

    tags = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={'class': 'form-control input-sm', 'placeholder': 'Tags, tags, tags', 'required': 'required'}))

    class Meta:
        model = Bookmark
        exclude = ['user']
        fields = ('title', 'link')
        widgets = {
            'title': forms.TextInput(
                attrs={'required': 'required', 'class': 'form-control input-sm', 'placeholder': 'Title'}),
            'link': forms.TextInput(
                attrs={'required': 'required', 'class': 'form-control input-sm', 'placeholder': 'Link'}),
        }

    def clean(self):
        cleaned_data = super(CreateBookmarkForm, self).clean()
        link = cleaned_data.get('link')

        ip_regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.[0-9]{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not ip_regex.match(link):
            raise forms.ValidationError(
                "Invalid URL. Please make sure your URL is valid."
            )

    def save(self, commit=True):
        bookmark = super(CreateBookmarkForm, self).save(commit=False)
        bookmark.title = self.cleaned_data['title']
        bookmark.link = self.cleaned_data['link']

        if commit:
            bookmark.save()

        return bookmark


class EditBookmarkForm(forms.ModelForm):

    tags = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={'class': 'form-control input-sm', 'placeholder': 'Tags, tags, tags', 'required': 'required'}))

    class Meta:
        model = Bookmark
        exclude = ['user']
        fields = ('title', 'link')
        widgets = {
            'title': forms.TextInput(
                attrs={'required': 'required', 'class': 'form-control input-sm', 'placeholder': 'Title'}),
            'link': forms.TextInput(
                attrs={'required': 'required', 'class': 'form-control input-sm', 'placeholder': 'Link'}),
        }

    def clean(self):
        cleaned_data = super(EditBookmarkForm, self).clean()
        link = cleaned_data.get('link')

        ip_regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.[0-9]{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not ip_regex.match(link):
            raise forms.ValidationError(
                "Invalid URL. Please make sure your URL is valid."
            )

    def save(self, commit=True):
        bookmark = super(EditBookmarkForm, self).save(commit=False)
        bookmark.title = self.cleaned_data['title']
        bookmark.link = self.cleaned_data['link']

        if commit:
            bookmark.save()

        return bookmark