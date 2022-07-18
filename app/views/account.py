"""用户登录"""

from django.shortcuts import render, redirect, HttpResponse
from django import forms
# from app import models
from app import models
from app.utils.md5 import md5
from app.utils import validCode


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
    validCode = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '密码','autocomplete':'off'}),

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
    # 获取验证码在session中存储的字符串
    valid_code_str = request.session.get("valid_code_str")
    print(request.session.get("valid_code_str"))

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'index.html', {'form': form})
    # if request.method == "POST":
    #     valid_code = request.POST.get('valid_code')
    #     valid_code_str = request.session.get("valid_code_str")
    #     print(request.session.get("valid_code_str"))

    form = LoginForm(data=request.POST, )

    # 对用户名密码进行验证
    if form.is_valid():

        # 获取用户输入的字符串
        enterValidCode = form.cleaned_data.pop('validCode')
        print(enterValidCode)

        # 验证成功，获取用户名和密码---字典

        # 数据库校验账户密码
        # 写法一
        # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        # 写法二
        # 注意模糊搜索内容里面字段必须与数据库里面字段名相同
        # print(request.session.get)

        # 判断验证码输入是否正确
        if valid_code_str != enterValidCode:
            form.add_error("validCode", "验证码输入错误")
            return render(request, 'index.html', {'form': form})

        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            # 主动添加报错信息
            form.add_error("password", "用户名或密码错误")
            return render(request, 'index.html', {'form': form})
        # 校验通过跳转界面

        # 网站生成随机字符串，写到用户浏览器cookie中。再输入到session
        # 数据会自动添加到django自动生成的`django_session`表中
        request.session["info"] = {'id': admin_object.id, 'username': admin_object.username}

        return redirect('/admin/list')

    return render(request, 'index.html', {'form': form})


def get_valid_code_img(request):
    """生成验证码图片"""
    img_data = validCode.get_valid_code_img(request)
    # #将图片验证码内容写到session中
    # request.session['img_data'] = img_data
    # #定义过期时间
    # request.session.set_expiry(60)
    # print(request.session.get("valid_code_str"))
    return HttpResponse(img_data)


def logout(request):
    """用户注销"""
    request.session.clear()
    return redirect('/login/')
