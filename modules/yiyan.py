import json
import requests
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel=Channel.current()

api='https://api.gmit.vip/Api/YiYan'
data={
    'format':'json'
}
header={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def yiyan(app:Ariadne, group:Group, message:MessageChain):
    """随机一言"""
    if message.display.strip() == '7':
        res=requests.get(api,data=data,headers=header).content
        if res:
            try:
                res=json.loads(res)
                if res['code'] == '200':
                    res_data = res.get('data_weather')
                    res_data_text = res_data.get('text')
                    await app.send_message(group,MessageChain(res_data_text))
                    return
                else:
                    await app.send_message(group,MessageChain('请求失败，请重试'))
                    return
            except Exception as e:
                await app.send_message(group,MessageChain(f'解析异常：{e}'))
                return
        else:
            await app.send_message(group,MessageChain('请求异常，请重试'))
            return
