# Generated by Django 3.2.13 on 2022-06-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220630_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=32, verbose_name='电话号')),
                ('price', models.IntegerField(default=100, max_length=64, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1, verbose_name='会员等级')),
                ('status', models.SmallIntegerField(choices=[(1, '未占用'), (2, '已占用')], default=1, verbose_name='是否占用')),
            ],
        ),
    ]