from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        witgets = {
            'title': forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Order'}),
        }
        labels = {
            'title':'', 'order': '', 'content': ''
        }