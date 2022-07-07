"""
自定义分页组件
"""
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        # 分页处理
        # 根据用户想要访问的页码计算出旗帜位置
        page = request.GET.get(page_param, "1")
        if page.isdecimal():  # 判断传参是否是整形
            page = int(page)
        else:
            page = 1
            print(page, type(page))
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
        # 首页
        first_page = '<li class="page-item"><a class="page-link" href="?page={}">{}</a></li>'.format(1, "首页")
        page_str_list.append(first_page)

        # 上一页
        if self.page > 1:
            up_page = '<li class="page-item"><a class="page-link" href="?page={}" aria-label="Previous"><span ' \
                      'aria-hidden="true">&laquo;</span></a></li> '.format(self.page - 1)
        else:
            up_page = '<li class="page-item"><a class="page-link" href="?page={}" aria-label="Previous"><span ' \
                      'aria-hidden="true">&laquo;</span></a></li> '.format(1)
        up_str_page = mark_safe("".join(up_page))
        page_str_list.append(up_str_page)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            down_page = '<li class="page-item"><a class="page-link" href="?page={}" aria-label="Next"><span ' \
                        'aria-hidden="true">»</span></a></li> '.format(self.page + 1)
        else:
            down_page = '<li class="page-item"><a class="page-link" href="?page={}" aria-label="Next"><span ' \
                        'aria-hidden="true">»</span></a></li> '.format(self.total_page_count)
        down_str_page = mark_safe("".join(down_page))
        page_str_list.append(down_str_page)


        # 尾页
        last_page = '<li class="page-item"><a class="page-link" href="?page={}">{}</a></li>'.format(
            self.total_page_count, "尾页")
        page_str_list.append(last_page)

        # 跳转
        search_page = """

           <form class="d-flex " role="search" method="get">
                 <input class="text" name="page" aria-label="Search"
                       >
                 <button class="page-link" type="submit" href="?page={}">跳转</button>
             </form>
         """.format(self.page)
        page_str_list.append(search_page)

        # 最后封装
        page_string = mark_safe("".join(page_str_list))  # mark_safe标记string为安全
        print(page_str_list)
        return page_string
