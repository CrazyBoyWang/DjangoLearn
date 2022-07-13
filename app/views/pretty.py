from django.shortcuts import render, redirect

from app import models
from app.forms.modelform import PrettyNum, PrettyNum_edit
from app.utils.pagination import Pagination


def prettynum_list(request):
    # 模糊搜索功能
    dict_list = {}
    search = request.GET.get("query", "")  # ""后面默认值为空值
    if search:
        dict_list["mobile__contains"] = search
    # 分页写法models.PrettyNum.objects.filter(**dict_list).order_by("-level")[0:10]
    queryset = models.PrettyNum.objects.filter(**dict_list).order_by("-level")
    page_object = Pagination(request, queryset)

    context = {
        'search': search,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html
    }

    # 通过会员等级方式倒叙排序，**dict_list为获取字典内容写法
    # info = models.PrettyNum.objects.filter(**dict_list).order_by("-level")
    return render(request, "prettynum_list.html", context)


def prettynum_add(request):
    if request.method == "GET":
        forms = PrettyNum()
        return render(request, "change.html", {"forms": forms,"title":'添加靓号'})
    forms = PrettyNum(data=request.POST)
    if forms.is_valid():
        forms.save()
        return redirect("/prettynum/list/")
    else:
        return render(request, "change.html", {"forms": forms,"title":'添加靓号'})


def prettynum_update(request, nid):
    prelist = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        pre = PrettyNum_edit(instance=prelist)
        return render(request, "prettynum_update.html", {'pre': pre})
    pre = PrettyNum_edit(data=request.POST, instance=prelist)
    if pre.is_valid():
        pre.save()
        return redirect("/prettynum/list/")
    else:
        return render(request, "prettynum_update.html", {'pre': pre})


def prettynum_delete(nid):
    models.PrettyNum.objects.filter(id=nid).delete()

    return redirect("/prettynum/list/")
