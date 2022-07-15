from django.shortcuts import render, redirect

from app import models
from app.utils.pagination import Pagination
from app.forms.modelform import AdminModelForm, AdminEditModelForm, AdminPwdRest


def admin_list(request):
    """管理员列表"""
    #判断用户是否已经登录
    #获取请求用户cookie字符串，判断在seesion中是否存在
    # info = request.session.get("info")
    # print(info)
    # if not info:
    #     return redirect("/login/")

    # 模糊搜索功能
    dict_list = {}
    search = request.GET.get("query", "")  # ""后面默认值为空值
    if search:
        dict_list["username__contains"] = search
    # 分页写法models.PrettyNum.objects.filter(**dict_list).order_by("-level")[0:10]
    queryset = models.Admin.objects.filter(**dict_list)
    page_object = Pagination(request, queryset)

    context = {
        'search': search,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html
    }
    # 搜索功能

    return render(request, 'admin_list.html', context)


def admin_add(request):
    """添加管理员"""
    if request.method == "GET":
        forms = AdminModelForm()
        return render(request, 'change.html', {'title': '添加管理员', 'forms': forms})
    forms = AdminModelForm(data=request.POST)
    if forms.is_valid():
        forms.save()
        print(forms.cleaned_data)  # 获取所有验证通过的参数信息
        return redirect("/admin/list/")

    return render(request, 'change.html', {'title': '添加管理员', 'forms': forms})


def admin_update(request, nid):
    title = "添加管理员"
    # 对象 / None
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:  # 如果为空 , 为了防止多用户操作的时候可能数据已经不存在了
        return render(request, "error.html", {'error': 'id不存在'})  # 可以自定意义一个错误页面

    if request.method == "GET":
        forms = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', {'forms': forms, 'title': title})
    forms = AdminEditModelForm(data=request.POST, instance=row_object)
    if forms.is_valid():
        forms.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'forms': forms, 'title': title})


def admin_delete(request, nid):
    nid_delete = models.Admin.objects.filter(id=nid).first()
    if not nid_delete:
        return render(request, 'error.html', {'error': 'id不存在或已删除'})
    else:
        nid_delete.delete()
        return redirect('/admin/list')


def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    print(row_object)
    title = "重置密码-{}".format(row_object.username)
    if not row_object:
        return render(request, 'error.html', {'error': 'id不存在'})

    if request.method == "GET":
        forms = AdminPwdRest(data=request.POST)
        return render(request, 'change.html', {'title': title,'forms':forms})
    forms = AdminPwdRest(data=request.POST,instance=row_object)
    if forms.is_valid():
        forms.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'title': title,'forms':forms})

