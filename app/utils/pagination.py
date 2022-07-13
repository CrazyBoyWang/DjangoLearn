"""
    自定义公共分页组件，可随时复用

    # 1、根据自己的情况去筛选自己的数据
    queryset = models.PrettyNum.objects.all()

    # 2、实例化分页对象
    page_object = Pagination(request,queryset)

    context = {
        'info': page_object.page_queryset,# 分完页的数据
        'page_string': page_object.html # 生成页码
    }
    return render(request, "prettynum_list.html",context)

    在html中展示页面代码

      {% for inf in queryset %}  # 循环数据量

        {% endfor %}
  <nav aria-label="Page navigation example">
            <ul class="pagination">
                {{ page_string }}
            </ul>
        </nav>

"""
import copy

from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        """
        :param request: 请求对象
        :param queryset: 查询符合条件的数据--根据数据进行分页
        :param page_size: 每页显示数据条数
        :param page_param: url中传递参数
        :param plus: 前后显示页签量
        """

        query_dict = copy.deepcopy(request.GET)  # 深拷贝数据
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param
        # self.query_dict.urlencode() 将请求参数拼接query=1&page=3

        # 分页处理
        # 根据用户想要访问的页码计算出起止位置
        page = request.GET.get(page_param, "1")
        if page.isdecimal():  # 判断传参是否是整形
            page = int(page)
        else:
            page = 1
            # print(page, type(page))
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        self.plus = plus
        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)  # 两数相除，余数为div
        if div:  # 如果有余数则页码要多+1
            total_page_count += 1
        self.total_page_count = total_page_count

    def html(self):
        # 计算当前页前5页和后5页

        if self.total_page_count <= 2 * self.plus + 1:  # 如果不满足长度则限制最大页数
            start_page = 1
            end_page = self.total_page_count
        else:  # 如果数据量过多。要判断0页之前问题
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页大于5
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []
        self.query_dict.setlist(self.page_param, [1])

        # print(self.query_dict.urlencode())
        # 首页
        first_page = '<li class="page-item"><a class="page-link" href="?{}">首页</a></li>'.format(
            self.query_dict.urlencode())
        page_str_list.append(first_page)

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            up_page = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span ' \
                      'aria-hidden="true">&laquo;</span></a></li> '.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            up_page = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span ' \
                      'aria-hidden="true">&laquo;</span></a></li> '.format(self.query_dict.urlencode())
        up_str_page = mark_safe("".join(up_page))
        page_str_list.append(up_str_page)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="page-item active"><a class="page-link" href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            down_page = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Next"><span ' \
                        'aria-hidden="true">»</span></a></li> '.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            down_page = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Next"><span ' \
                        'aria-hidden="true">»</span></a></li> '.format(self.query_dict.urlencode())
        down_str_page = mark_safe("".join(down_page))
        page_str_list.append(down_str_page)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        last_page = '<li class="page-item"><a class="page-link" href="?{}">尾页</a></li>'.format(
            self.query_dict.urlencode())
        page_str_list.append(last_page)

        # 跳转
        search_page = """

           <form class="d-flex " role="search" method="get">
                 <input class="text" name="page" aria-label="Search"
                       >
                 <button class="page-link" type="submit" href="?{}">跳转</button>
             </form>
         """.format(self.page)
        page_str_list.append(search_page)

        # 最后封装
        page_string = mark_safe("".join(page_str_list))  # mark_safe标记string为安全
        # print(page_str_list)
        return page_string
