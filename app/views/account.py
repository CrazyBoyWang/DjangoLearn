"""用户登录"""

from django.shortcuts import render, redirect
from django import forms
# from app import models


# forms写法

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
    )


# modelForms
# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ["username","password"]

def login(request):
    form = LoginForm()
    return render(request, 'index.html',{'form':form})
