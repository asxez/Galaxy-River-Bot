import asyncio
import base64
import json
import os
import random
import re

import config
import requests
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel=Channel.current()

url = "https://flagopen.baai.ac.cn/flagStudio/v1/text2img"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "token": config.AI_IMAGE_KEY
}

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def image(app:Ariadne, group:Group, message:MessageChain):
    """
    二次元图片
    :param app:
    :param group:
    :param message:
    :return:
    """
    data={
        'format':'json'
    }
    header={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
    }
    if message.display.strip() == '3':
        res=requests.get('https://api.gmit.vip/Api/DmImg',data=data,headers=header).content
        if res:
            try:
                res=json.loads(res)
                if res['code'] == '200':
                    res_data = res.get('data_weather')
                    res_data_url = res_data.get('url')
                    await asyncio.sleep(1.0)
                    name=re.findall('dm/(.*?).jpg',res_data_url,re.S)[0]
                    byte=requests.get(res_data_url).content
                    with open(f'./modules/data/imgs/{name}.jpg','wb') as f:
                        f.write(byte)
                    await app.send_message(group,MessageChain(Image(path=f'./modules/data/imgs/{name}.jpg')))
                    return
                else:
                    await app.send_message(group,MessageChain('请求失败，请重试'))
                    return
            except Exception as e:
                await app.send_message(group,MessageChain(f'解析异常:{e}'))
                return
        else:
            await app.send_message(group,MessageChain('请求异常，请重试'))
            return
    else:
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def ai_image(app:Ariadne, group:Group, message:MessageChain):
    """
    AI生成的图片（已剔除露点）
    :param app:
    :param group:
    :param message:
    :return:
    """
    if message.display.strip() == '8':
        num = random.randint(1,196)
        await app.send_message(group,MessageChain(Image(path=f'./modules/data/pictures/{num}.png')))
        return
    else:
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def ai_image(app:Ariadne, group:Group, message:MessageChain):
    """
    ai绘图（仅支持动漫）
    其中的存储图片的地方需要你修改，在第101和102行
    :param app:
    :param group:
    :param message:
    :return:
    """
    if message.display.strip().split(' ')[0] == '/aip':
        payload = {
            "prompt": message.display.strip().split(' ')[1],
            "guidance_scale": 10,
            "height": 512,
            "negative_prompts": "",
            "sampler": "ddim",
            "seed": 1024,
            "steps": 60,
            "style": "动漫",
            "upsample": 1,
            "width": 512
        }
        if os.path.exists(f"F:/WorkSpace/py-case/cs/modules/data/imgs/{message.display.strip().split(' ')[1]}.jpg"):
            await app.send_message(group,MessageChain(Image(path=f"F:/WorkSpace/py-case/cs/modules/data/imgs/{message.display.strip().split(' ')[1]}.jpg")))
            return
        else:
            try:
                res = requests.post(url,json=payload,headers=headers).content
                res=json.loads(res).get('data')
                data=base64.b64decode(res)
                with open(f"./modules/data/imgs/{message.display.strip().split(' ')[1]}.jpg",'wb') as f:
                    f.write(data)
                await app.send_message(group,MessageChain(Image(path=f"./modules/data/imgs/{message.display.strip().split(' ')[1]}.jpg")))
                return
            except:
                await app.send_message(group,MessageChain('请求异常，请重试'))
                return
    else:
        return
