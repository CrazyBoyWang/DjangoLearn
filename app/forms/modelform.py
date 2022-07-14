from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app import models
from app.utils.bootstrap import BootstrapModelForm
from app.utils.md5 import md5


class MyForm(BootstrapModelForm):
    # 下面为通用校验方式，入过对某些字段进行单独校验需要使用原始写法
    # create_time = forms.DateField(verbose_name="入职时间")
    # create_time.widget_attrs = {"class":"input-group date", "data-provide":"datepicker"}
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


# 验证手机号输入是否正确
class PrettyNum(BootstrapModelForm):
    mobile = forms.CharField(  # 单独校验规则，。关于手机号正则校验
        label="电话号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号输入错误')],

    )

    class Meta:
        model = models.PrettyNum
        fields = "__all__"  # 表示显示自定义的所有字段
        # exclude = ['name'] # 表示排除哪个字段

    #  钩子方法 手机号不能重复
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']  # 获取对应的字段
        # exits = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=mobile).exists()
        exits = models.PrettyNum.objects.filter(mobile=mobile).exists()
        if exits:
            raise ValidationError("该手机号码已存在")
        return mobile


class PrettyNum_edit(BootstrapModelForm):
    mobile = forms.CharField(  # 单独校验规则，。关于手机号正则校验
        label="电话号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号输入错误')],

    )

    class Meta:
        model = models.PrettyNum
        fields = "__all__"  # 表示显示自定义的所有字段
        # exclude = ['name'] # 表示排除哪个字段

    #  钩子方法 手机号不能重复，查找排除自身之外的手机还是否有重复
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']  # 获取对应的字段
        exits = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=mobile).exists()
        if exits:
            raise ValidationError("该手机号码已存在")
        return mobile


class AdminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_password(self):  # 先对密码进行加密
        password = self.cleaned_data.get("password")
        return md5(password)

    # 钩子方法 判断密码是否一致
    def clean_confirm_password(self):
        print(self.cleaned_data.get("confirm_password"))
        password = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != password:
            raise ValidationError("密码不一致")
        # 返回值是验证通过之后返回的时什么保存到数据库中就是什么
        return confirm


class AdminEditModelForm(BootstrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']


class AdminPwdRest(BootstrapModelForm):
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        # widgets = {
        #     'password': forms.PasswordInput,
        # }

    def clean_password(self):  # 先对密码进行加密
        password = self.cleaned_data.get("password")
        md5_pwd = md5(password)
        #判断密码是否和以前一致
        exist =models.Admin.objects.filter(id=self.instance.pk,password=md5_pwd).exists()
        if exist:
            raise ValidationError("密码不能一致")
        return md5_pwd

    # 钩子方法 判断密码是否一致
    def clean_confirm_password(self):
        print(self.cleaned_data.get("confirm_password"))
        password = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != password:
            raise ValidationError("密码不一致")
        # 返回值是验证通过之后返回的时什么保存到数据库中就是什么
        return confirm

