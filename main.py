setting = {
    "align": "center", # 글자 위치 center, (right|left)-(top|bottom)
    "base": "base.png", # 배경 이미지
    "background-color": "", # base가 없는 경우 단색으로 처리
    "font": "Galmuri14.ttf", # 폰트
    "font_size": 40, # 글자 크기
    "font_color": "black" # 글자 색상
}












from PIL import Image, ImageDraw, ImageFont, ImageColor
import random, json, ctypes, os
msg = random.choice(json.load(open("message.json", encoding="utf-8")))



if not setting["base"]:
    im = Image.new("RGB", (1920, 1080))

else:
    try:
        im = Image.open(setting["base"])
    except:
        raise Exception("'base'옵션이 올바르지 않습니다. :", setting["base"])
W, H = im.size
draw = ImageDraw.Draw(im)

font = ImageFont.truetype(setting["font"], setting["font_size"])

w, h = draw.textsize(msg, font=font)
draw.rectangle((0, 0, W, H), fill=(lambda x: ImageColor.getrgb(x) if x else None)(setting["background-color"]), width=0)
if setting["align"] == "center":
    draw.text(((W-w)/2,(H-h)/2), msg, fill=setting["font_color"],font=font)

elif setting["align"] == "left-top":
    draw.text((10, 10), msg, fill=setting["font_color"],font=font)

elif setting["align"] == "left-bottom":
    draw.text((10, H-h-10), msg, fill=setting["font_color"],font=font)

elif setting["align"] == "right-top":
    draw.text((W-w-10, 10), msg, fill=setting["font_color"],font=font)

elif setting["align"] == "right-bottom":
    draw.text((W-w-10, H-h-10), msg, fill=setting["font_color"],font=font)

else:
    raise Exception("'align'옵션이 올바르지 않습니다. :", setting["align"])

im.save("wallpaper.png", "PNG")

lpszImage = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpaper.png")

ctypes.windll.user32.SystemParametersInfoW(20, 0, lpszImage , 3)