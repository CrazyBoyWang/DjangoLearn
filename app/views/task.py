import json

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app import models
from app.utils.bootstrap import BootstrapModelForm
from app.utils.pagination import Pagination


class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"


def task_list(request):
   # 数据库中获取所有任务
   queryset = models.Task.objects.all().order_by("-id")
   page_object = Pagination(request,queryset)
   form = TaskModelForm()
   context = {
    "form": form,
    "queryset": page_object.page_queryset,
    "page_string": page_object.html()

   }
   return render(request, "task_list.html", context)


# 去除token验证装饰器
@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    # json_string = json.dumps(data_dict)
    # return HttpResponse(json_string)
    # 同理
    # 对数据信息进行校验
    data_dict = {"status": True}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))


# @csrf_exempt
# def task_add(request):
#     # 对数据进行校验
#     print(request.POST)
#     form = TaskModelForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#         data_dict = {"status": True}
#         return HttpResponse(json.dumps(data_dict))
#     # print(type(form.ErrorDict))
#     # 输入错误返回报错信息
#
#     data_dict = {"status": False, 'error': form.errors}
#     # print(form.errors)
#     return HttpResponse(json.dumps(data_dict, ensure_ascii=False))

# ajax对于提交表单数据进行校验方法
@csrf_exempt
def task_add(request):
    # 对数据进行校验
    print(request.POST)
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False,'error':form.errors}
    return HttpResponse(json.dumps(data_dict))
