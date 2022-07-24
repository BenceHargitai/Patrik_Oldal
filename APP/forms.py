from django import forms

class EditForm(forms.Form):
    cim = forms.CharField()
    leiras = forms.CharField()
    url = forms.URLField()
