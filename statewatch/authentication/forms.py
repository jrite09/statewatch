from django import forms

class AccountForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()