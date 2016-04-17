'''
Created on 17 de abr. de 2016

@author: alvar
'''
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)