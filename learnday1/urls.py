"""learnday1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import depart,pretty,users,admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    #部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    # http://127.0.0.1:8000/<int:nid>/depart/update/ 默认以后传值中间必须有这个数字
    path('depart/<int:nid>/update/', depart.depart_update),

    #用户管理
    path('user/list/', users.user_list),
    path('user/add/',users.user_add),
    path('user/<int:nid>/update/',users.user_update),
    path('user/<int:nid>/delete/',users.user_delete),


    # 靓号管理
    path('prettynum/list/',pretty.prettynum_list),
    path('prettynum/add/', pretty.prettynum_add),
    path('prettynum/<int:nid>/update/', pretty.prettynum_update),
    path('prettynum/<int:nid>/delete/', pretty.prettynum_delete),

    #管理员管理
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),

    path('admin/<int:nid>/update/', admin.admin_update),

]
