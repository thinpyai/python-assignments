from django import forms
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from .models import Book
# from bootstrap_datepicker_plus import DatePickerInput


class BookForm(forms.ModelForm):
    class Meta:
        model = Book        
        fields = ('title', 'author', 'publisher', 'summary', 'category', 'release_date')