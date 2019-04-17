import fnmatch
import os.path
import tweepy
import os
from google_images_download import google_images_download
from Pillow import Image, ImageFont, ImageDraw
from words import noun
C_KEY = " "
C_SECRET = " "
A_TOKEN = " "
A_TOKEN_SECRET = " "

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)


vowels = "aeiou"
if (noun[0]) in vowels:
    article = "an"
else:
    article = "a"

response = google_images_download.googleimagesdownload()
arguments = {"keywords": noun, "limit": 1, "format": "png", "color_type":"transparent", "type":"photo", "output_directory": os.path.join("C:/", "Users", "Matthew", "PycharmProjects", "TwitterBot", "botImages", ), "no_directory":"true", "no_numbering":"true","aspect_ratio": "square"}#
response.download(arguments)

for file in os.listdir("C:/Users/Matthew/PycharmProjects/TwitterBot/botImages"):
    if fnmatch.fnmatch(file, '*.png'):
        print(file)

def tweet_image(message):
    font = ImageFont.truetype(font ="PlainPensle_BoldItalic.ttf", size=75)
    W, H =(1280,720)
    w, h = font.getsize(message)
    img = Image.new('RGB', (W,H), color= (240, 226, 179))
    img_w, img_h = img.size

    draw = ImageDraw.Draw(img)
    draw.text(((W-w)/2,585), message, font=font, fill='black')

    img2 = Image.open(os.path.join("C:/Users/Matthew/PycharmProjects/TwitterBot/botImages", file), 'r')
    img2 = img2.resize((500,500))

    img3 = img2.convert("RGBA")
    img3.resize((500,500))

    offset = (390, 65)
    img.paste(img3, offset, mask=img3)

    img.save('temp.png')
    os.remove(os.path.join("C:/Users/Matthew/PycharmProjects/TwitterBot/botImages", file))
    api.update_with_media('temp.png', status=message)

message = "This is not " + article + " " + noun + "."
#tweet_image(message)