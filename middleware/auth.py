from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, render


# 中间件解决界面鉴权问题
class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 排除不需要登录session就可以访问的页面，要不会产生多次重定向
        url_path = [
            '/login/',
            '/blog/get_valid_code_img/',
        ]
        # print(request.path_info)
        if request.path_info in url_path:
            return None

        # 1、读取当前访问用户的session信息，如果获取成功测代表登录过
        # 在中间件中如果有返回值，直接进行返回，返回内容可以是httpResponse、render、redirect
        info_dict = request.session.get("info")

        if info_dict:
            # 如果为None则中间件继续执行。
            return None
        else:
            # 如果有值则中间件直接返回。则直接返回到登录页面去
            return redirect("/login/")
