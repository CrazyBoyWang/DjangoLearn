from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app import models
from app.utils.bootstrap import BootstrapModelForm


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
