from django.shortcuts import render, redirect
from app import models
from django import forms


class MyForm(forms.ModelForm):
    # 下面为通用校验方式，入过对某些字段进行单独校验需要使用原始写法
    class Meta:
        model = models.UserInfo
        fields = [
            "name",
            "password",
            "age",
            "account",
            "create_time",
            "depart",
            "gender"
        ]

    # 自定义全局样式
    # 重新定义init方法。执行父类init方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():  # 如果不想增加某个插件可以通过if来判断
            print(name, field)
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}  # 定义插件方法


# Create your views here.
def depart_list(request):
    """部门列表"""
    # 数据库中获取所有部门列表
    # queryset 是列表,每一个是封装了一行数据
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    # queryset 是列表,每一个是封装了一行数据
    queryset = models.Department.objects.all()

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


# 用户列表
def user_list(request):
    """用户列表"""
    userinfo = models.UserInfo.objects.all()
    # python获取字段内容
    # for obj in userinfo:
    #     print(obj.create_time.strftime("%Y-%m-%d"))
    #     print(obj.get_gender_display())  # 根据创建的元组数据反向搜索对应的中文内容
    #     print(obj.depart.title)  # 获取数据库存储字段值,如果是关联表可以通过定义的depart去获取关联表内容

    return render(request, "user_list.html", {'userinfo': userinfo})


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


def user_update(request,nid):
    #根据id获取数据
    if request.method=="GET":

        user_ojb = models.UserInfo.objects.filter(id = nid).first() # 查询要修改的数据信息
        form = MyForm(instance=user_ojb) # 将要修改的信息赋值在ModelForm插件中并在前端展示

        return render(request, "user_update.html", {'nid': nid,'form':form})
    user_ojb = models.UserInfo.objects.filter(id=nid).first()  # 查询要修改的数据信息
    form = MyForm(request.POST,instance=user_ojb)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    else:
       print( form.errors.as_json())


