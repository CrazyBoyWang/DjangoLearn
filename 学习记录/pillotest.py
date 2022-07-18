from pil import Image, ImageFont
from pil.ImageDraw import ImageDraw

img = Image.new(mode='RGB', size=(110, 110), color=(255, 255, 0))

draw = ImageDraw(img, mode='RGB')

font = ImageFont.truetype("simhei.ttf", 30)
draw.text([0, 0], "test", "red")
with open('test.png', 'wb') as f:
    img.save(f, format='png')
