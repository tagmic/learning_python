#PIL python image library
##PIL的imageDraw提供了一系列的绘图方法，例如生成字母
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#生成随机字母
def random_char():
    return chr(random.randint(65,90))
#随机颜色
def random_color_1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def random_color_2():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#240*60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font=ImageFont.truetype('NimbusRomNo9T.ttf',36)
#创建draw对象
draw=ImageDraw.Draw(image)
#将图片定义区域填充像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=random_color_1())
#绘制文字
for t in range(4):
    try:
        draw.text((60*t+10,10),random_char(),font=font,fill=random_color_2())
    except BaseException as e:
        print('exception----',e)
#保存
image.save('code.jpg','jpeg')
