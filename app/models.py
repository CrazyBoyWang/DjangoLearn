from django.db import models


# Create your models here.


class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='标题')  # verbose_name注解

    # 定制对象返回内容，指定返回信息
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(max_length=16, verbose_name="姓名")
    password = models.CharField(max_length=64, verbose_name="密码")
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)  # 精准小数

    create_time = models.DateField(verbose_name="入职时间")

    # 无约束写法
    # depart_id = models.BigIntegerField(verbose_name="部门id")

    # 有约束写法
    # 员工表中只能存在已经存在的部门id---to表示与哪张表关联，to_fields表示关联的字段名
    # 如果关联的话。depart生成阶段会自动生成数据列depart_id
    # depart = models.ForeignKey(to="Department", to_fields="id")

    # 级联删除-->部门被删除，对应的员工也删除
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)

    # 部门被删除，对应的用户置空
    depart = models.ForeignKey(verbose_name="部门", to="Department", null=True, blank=True, to_field="id",
                               on_delete=models.SET_NULL)

    # 性别->在django中做约束方法
    gender_choices = ((1, "男"), (0, "女"))
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


"""
    1、标准数据库范式--关联表存id信息，可以节省数据库开销，但需要链表根据id查询到对应的数据
    2、如果提高性能，可以降低链表查询情况。直接存储对应想要的内容
    本次练习存储id方式
    
    数据库表约束
    
    如果部门被删除
    1、删除用户-->级联删除
    2、置空部门id
    
"""


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name="电话号", max_length=32)
    price = models.IntegerField(verbose_name="价格",default=100)
    level_choice = (
        (1, "初级"),
        (2, "中级"),
        (3, "高级"),
    )

    level = models.SmallIntegerField(verbose_name="会员等级", choices=level_choice,default=1)
    status_choice =(
        (1, "未占用"),
        (2, "已占用")
    )
    status = models.SmallIntegerField(verbose_name="是否占用", choices=status_choice, default=1)
