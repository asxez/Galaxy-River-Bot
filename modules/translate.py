import json
import requests
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel=Channel.current()

header={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def translate(app:Ariadne, group:Group, message:MessageChain):
    global res
    try:
        if message.display.strip().split(' ')[0] == '/tra' and message.display.strip().split(' ')[1] and message.display.strip().split(' ')[2]:
            api='https://api.gmit.vip/Api/Translate'
            data_en={
                'format':'json',
                'text':message.display.strip().split(' ')[2],
                'from':'auto',
                'to':'en'
            }
            data_zh_CN={
                'format':'json',
                'text':message.display.strip().split(' ')[2],
                'from':'auto',
                'to':'zh'
            }
            if message.display.strip().split(' ')[1] == 'en':
                res = requests.get(api,params=data_en).content
            elif message.display.strip().split(' ')[1] == 'zh':
                res =requests.get(api,params=data_zh_CN).content
            else:
                await app.send_message(group,MessageChain('暂不支持此语言'))
            if res:
                res = json.loads(res)
                if res['code'] == '200':
                    text = res.get('data_weather').get('result')
                    await app.send_message(group,MessageChain(f'翻译结果为:{text}'))
                    return
                else:
                    await app.send_message(group,MessageChain('访问超时，请重试'))
                    return
            else:
                await app.send_message(group,MessageChain('访问失败，请重试'))
                return
        else:
            return
    except:
        return
