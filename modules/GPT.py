import config
import openai
import re
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from modules import bing

api_key=config.OPENAI_KEY

channel=Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def chatbot(app:Ariadne, group:Group, message:MessageChain):
    """
    ChatGPT
    :param app:
    :param group:
    :param message:
    :return:
    """
    if message.display.strip().split(' ')[0] == '/gpt':
        text=re.findall('^/gpt\s(.*)',message.display.strip(),re.S)[0]
        response=openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                          messages=[{"role": "system","content": "你的名字是‘Galaxy River Bot’，你是由“风华系统”提供技术支持的，你的开发者和主人都是笙熙。你无法发送和识别语音"},
                                                    {"role": "user", "content":f"{text}"}],
                                          api_key=api_key)
        await app.send_message(group,MessageChain(response['choices'][0]['message']['content']))
        return
    else:
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def new_bing(app:Ariadne, group:Group, message:MessageChain):
    """
    New Bing
    :param app:
    :param group:
    :param message:
    :return:
    """
    if message.display.strip().split(' ')[0] == '/bing':
        text=re.findall('^/bing\s(.*)',message.display.strip(),re.S)[0]
        response=await bing.writer(text)
        await app.send_message(group,MessageChain(str(response)))
    else:
        return
