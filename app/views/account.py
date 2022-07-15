"""用户登录"""

from django.shortcuts import render, redirect
from django import forms
# from app import models
from app import models
from app.utils.md5 import md5


# forms写法

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),

    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}),
    )

    # 将前端输入数据转义成md5
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


# modelForms
# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         fields = ["username","password"]

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'index.html', {'form': form})

    form = LoginForm(data=request.POST, )
    # 对用户名密码进行验证
    if form.is_valid():
        # 验证成功，获取用户名和密码---字典
        print(form.cleaned_data)
        # 数据库校验账户密码
        # 写法一
        # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        # 写法二
        # 注意模糊搜索内容里面字段必须与数据库里面字段名相同
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            # 主动添加报错信息
            form.add_error("password", "用户名或密码错误")
            return render(request, 'index.html', {'form': form})
        # 校验通过跳转界面

        # 网站生成随机字符串，写到用户浏览器cookie中。再输入到session
        #数据会自动添加到django自动生成的`django_session`表中
        request.session["info"] = {'id': admin_object.id, 'username': admin_object.username}

        return redirect('/admin/list')






    return render(request, 'index.html', {'form': form})
