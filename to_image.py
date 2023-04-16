from PIL import Image, ImageDraw, ImageFont

def create(text,max_len):
    fontSize = 50
    liens = text.split('\n')
    image = Image.new('RGB', ((fontSize * max_len), len(liens) * (fontSize + 5)), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('./ttf/字语时光体.ttf',45)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    draw.text((40,5), text=text, font=font,fill='#000000')
    image.save(f'./modules/data/answer/code.png', 'png')


'''''
with open('cs.txt','w') as f:
    f.write(text)

with open('cs.txt','r') as f:
    text_temp=f.readlines()
max_len = 0
for i, s in enumerate(text_temp):
    if len(s) > max_len:
        max_len = len(s)
create(text,max_len)
'''''
