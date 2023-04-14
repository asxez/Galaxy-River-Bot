import asyncio
import os
import sys

from creart import create
from graia.ariadne.app import Ariadne, Broadcast
from graia.ariadne.app import GroupMessage
from graia.ariadne.connection.config import config, HttpClientConfig, WebsocketClientConfig
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Saya

import config as c

saya=create(Saya)
bcc=create(Broadcast)

app = Ariadne(
    connection=config(
        c.BOT_QQ,
        c.verifyKey,
        # 默认为 "http://localhost:8080"
        # 如果你 mirai-api_weather-http 的地址与端口是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api_weather-http 的地址与端口
        HttpClientConfig(host=c.http),
        WebsocketClientConfig(host=c.ws)
    ),
)

"""
模块加载
"""
with saya.module_context():
    saya.require('modules.image')
    saya.require('modules.music')
    saya.require('modules.start')
    #saya.require('modules.search_image')
    saya.require('modules.yiyan')
    saya.require('modules.GPT')
    saya.require('modules.manage')
    #saya.require('modules.test')
    saya.require('modules.back_end')
    saya.require('modules.translate')
    saya.require('modules.scheduler')
    saya.require('modules.majors')


@bcc.receiver(GroupMessage)
async def clean(app1:Ariadne, group:Group, message:MessageChain):
    """
    清除new bing记忆
    此处采用重启程序的方法清除
    :param app1:
    :param group:
    :param message:
    :return:
    """
    if message.display.strip() == '/clean':
        await app1.send_message(group, MessageChain('记忆已清除，请等待几秒钟'))
        await asyncio.sleep(1)
        python=sys.executable
        os.execl(python,python,*sys.argv)
    else:
        return

app.launch_blocking()
