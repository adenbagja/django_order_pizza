from django import forms

class SearchForm(forms.Form):
    s = forms.CharField(label='search', max_length=100)