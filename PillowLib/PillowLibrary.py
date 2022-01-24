from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

# ************************************ write text on image  * ************************************
img1 = Image.open('2.jpg')
draw = ImageDraw.Draw(img1)
font = ImageFont.truetype("arial.ttf", 500)
points = (100, 100)
string = "Prince Kirad"
txtColor = "white"
draw.text(points, string, txtColor, font=font)
img1.save('one.jpg')


# size_300 = (300, 300)

# # save multiple file in folder
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         i.thumbnail(size_300)
#         i.save('300/{}_300{}'.format(fn, fext))  #change size image
#         # i.save('img/{}.png'.format(fn))    # another ext

# img1.show('1.jpeg')       #open image into picture viewer
# img1.save('one.png')      #change format of 
# img1.rotate(90).save('2_mod.jpg')    #rotate image
# img1.convert(mode="L").save('2_mod.jpg')    #black and white image
# img1.filter(ImageFilter.GaussianBlur(15)).save('2_mod.jpg')     # blur image

