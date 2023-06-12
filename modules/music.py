import json
import re
from pathlib import Path

import graiax.silkcoder as silkcoder
import requests
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Voice
from graia.ariadne.message.parser.base import ContainKeyword
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graiax.silkcoder import ffmpeg

from . import get_wyy_id

channel=Channel.current()

ffmpeg.set_ffmpeg_path('F:\\asxe\\ffmpeg\\bin\\ffmpeg.exe')

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def kw(app:Ariadne, group:Group, message:MessageChain):
    """
    kw
    :param app:
    :param group:
    :param message:
    :return:
    """

    if ContainKeyword('/kw') and message.display.strip().split(' ')[0] == '/kw':
        get_name=message.display.strip().split(' ')
        if get_name[1]:
            name=get_name[1]
            url = 'http://search.kuwo.cn/r.s?all=' + name + '&ft=music& itemset=web_2013&client=kt&pn={1}&rn={2}&rformat=json&encoding=utf8'
            res = requests.get(url,headers=header)
            res.encoding = 'utf-8'
            get_id = re.findall('(MUSIC_\d+)', res.text)
            URL = requests.get('http://antiserver.kuwo.cn/anti.s?type=convert_url&rid=' + get_id[0] + '&format=aac|mp3&response=url',headers=header)
            Data = requests.get(str(URL.text),headers=header).content
            with open(f'./modules/data_weather/music/{name}.mp3', mode='wb') as f:
                f.write(Data)
            byte=await silkcoder.async_encode(Path(f'./modules/data_weather/music/{name}.mp3'))
            await app.send_message(group,MessageChain(Voice(data_bytes=byte)))
            await app.send_message(group,MessageChain('由于资金原因，音乐功能调用免费版，存在瑕疵！'))
            return
        else:
            return
    else:
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def wyy(app:Ariadne, group:Group, message:MessageChain):
    """
    wyy
    :param app:
    :param group:
    :param message:
    :return:
    """

    api='https://api.gmit.vip/Api/Netease'
    if ContainKeyword('/wyy') and message.display.strip().split(' ')[0] == '/wyy':
        get_name=message.display.strip().split(' ')
        if get_name[1]:
            get_id=(get_wyy_id.Music_api().get_music_list(get_name[1]))[0].get('id')
            data = {
                'format': 'json',
                'id':get_id
            }
            res=requests.get(api,params=data,headers=header).content
            if res:
                try:
                    res=json.loads(res)
                    if res['code'] == 200:
                        res_data=res.get('data_weather')
                        res_data_author=res_data.get('author')
                        res_data_title=res_data.get('title')
                        res_data_url=res_data.get('url')
                        music_b=requests.get(res_data_url,headers=header).content
                        with open(f'./modules/data_weather/music/{res_data_title}_{res_data_author}.mp3','wb') as f:
                            f.write(music_b)
                        byte=await silkcoder.async_encode(Path(f'./modules/data_weather/music/{res_data_title}_{res_data_author}.mp3'))
                        await app.send_message(group,MessageChain(Voice(data_bytes=byte)))
                        await app.send_message(group,MessageChain(f'歌名：{res_data_title}\n作者：{res_data_author}'))
                        return
                    else:
                        await app.send_message(group,MessageChain('解析失败，请重试'))
                        return
                except:
                    await app.send_message(group,MessageChain('连接出错，请重试'))
                    return
            else:
                return
