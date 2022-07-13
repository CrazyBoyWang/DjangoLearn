from django.shortcuts import render, redirect

from app import models
from app.forms.modelform import MyForm
from app.utils.pagination import Pagination


# 用户列表
def user_list(request):
    """用户列表"""
    queryset = models.UserInfo.objects.all()
    # python获取字段内容
    # for obj in userinfo:
    #     print(obj.create_time.strftime("%Y-%m-%d"))
    #     print(obj.get_gender_display())  # 根据创建的元组数据反向搜索对应的中文内容
    #     print(obj.depart.title)  # 获取数据库存储字段值,如果是关联表可以通过定义的depart去获取关联表内容
    user_page = Pagination(request, queryset)
    context = {
        'userinfo': user_page.page_queryset,
        'user_page': user_page.html()
    }

    return render(request, "user_list.html", context)


def user_add(request):
    # 对数据库操作用modelform  非数据库操作使用form
    if request.method == "GET":
        form = MyForm()
        return render(request, "user_add.html", {"form": form})

    # post提交数据，数据校验
    form = MyForm(data=request.POST)
    if form.is_valid():  # 校验不为空
        print(form.cleaned_data)
        form.save()  # 自动保存数据库
        return redirect("/user/list/")
    else:
        # 如果校验失败会有错误信息提示
        print(form.errors)
        return render(request, "user_add.html", {"form": form})


def user_update(request, nid):
    # 根据id获取数据
    user_ojb = models.UserInfo.objects.filter(id=nid).first()  # 查询要修改的数据信息
    if request.method == "GET":
        form = MyForm(instance=user_ojb)  # 将要修改的信息赋值在ModelForm插件中并在前端展示
        return render(request, "user_update.html", {'nid': nid, 'form': form})
    form = MyForm(request.POST, instance=user_ojb)
    if form.is_valid():
        # form.instance.字段名= 数据 如果想添加别的字段的内容
        form.save()
        return redirect("/user/list/")
    else:
        print(form.errors.as_json())
        return render(request, "user_update.html", {'nid': nid, 'form': form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
