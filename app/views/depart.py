from django.shortcuts import render, redirect

from app import models
from app.utils.pagination import Pagination


# Create your views here.
def depart_list(request):
    """部门列表"""
    # 数据库中获取所有部门列表
    # queryset 是列表,每一个是封装了一行数据
    queryset = models.Department.objects.all()
    depart_page = Pagination(request,queryset)
    context = {
        'queryset': depart_page.page_queryset,
        'depart_page':depart_page.html()
    }

    return render(request, "depart_list.html", context)


def depart_add(request):
    """添加部门"""
    # queryset 是列表,每一个是封装了一行数据
    # queryset = models.Department.objects.all()

    if request.method == "GET":
        return render(request, "depart_add.html")
    # 获取用户提交数据 如果title为空呢？

    title = request.POST.get("title")
    # 保存数据库
    models.Department.objects.create(title=title)
    # 重定向会部门列表
    return redirect("/depart/list/")


def depart_delete(request):
    # 删除功能
    nid = request.GET.get('nid')
    # 删除
    models.Department.objects.filter(id=nid).delete()
    # 跳转会列表
    return redirect("/depart/list/")


# 进来多加一个参数。nid 会直接传值过来
def depart_update(request, nid):
    # 修改部门,根据nid获取数据,获取的是一行数据
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_update.html", {"row_object": row_object})
    # 根据用户提交标题更新数据
    title = request.POST.get("title")
    # 修改成功之后重定向的到列表页面
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")

