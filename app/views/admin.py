from django.shortcuts import render, redirect

from app import models


def admin_list(request):
    """管理员列表"""
    queryset = models.Admin.objects.all()
    return render(request,'admin_list.html',{'queryset':queryset})
