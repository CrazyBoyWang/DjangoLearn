import random
from pil import Image, ImageDraw, ImageFont
from io import BytesIO  # 缓存方法
import random

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_valid_code_img(request):
    # 方式:

    img = Image.new("RGB", (270, 40), color=get_random_color())  # 生成一个宽270*高40的画布，背景颜色随机
    draw = ImageDraw.Draw(img)  # 进行绘画
    kumo_font = ImageFont.truetype("app/static/font/simhei.ttf", size=32)  # 字体 字体大小
    valid_code_str = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))  # 0-9的随机数 9
        random_low_alpha = chr(random.randint(97, 122))  # a 到 z 随机的一个小写字母 b
        random_upper_alpha = chr(random.randint(65, 90))  # A 到 Z 随机的一个大写字母 Q
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])  # 2
        draw.text((i * 50 + 20, 5), random_char, get_random_color(), font=kumo_font)  # 往长方形上写字
        # 保存验证码字符串
        valid_code_str += random_char  # 85656
    width = 270
    height = 40
    for i in range(10):
        # draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())#画小点
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())  # 小线段
    # print(valid_code_str)
    #将验证码信息存在session中
    request.session["valid_code_str"] = valid_code_str
    # #定义过期时间
    request.session.set_expiry(60)
    f = BytesIO()
    img.save(f, "png")  # png
    data = f.getvalue()

    return data
