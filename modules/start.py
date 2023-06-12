import asyncio

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

from .. import config

channel=Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def start(app:Ariadne, group:Group, member:Member, message:MessageChain):
    """
    菜单
    :param app:
    :param group:
    :param member:
    :param message:
    :return:
    """
    if message.display.strip() == '菜单':
        #菜单
        await app.send_message(group,MessageChain(Image(path=f'./modules/功能.png')))
        return

    elif message.display.strip() == '1':
        #chatgpt
        await app.send_message(group,MessageChain('指令：/gpt 问题\n例：/gpt 你是谁？你是由谁开发的？\n(请使用一句话描述出你的需求，因资金原因，本机并未开发具有上下文的AI)'))
        return

    elif message.display.strip() == '2':
        #new bing
        await app.send_message(group,MessageChain('指令：/bing 问题\n此功能具有记忆，请在使用完后输入“/clean”\n本功能响应较慢，使用时请耐心等待！'))
        return

    elif message.display.strip() == '4':
        #音乐
        await app.send_message(group,MessageChain('当前支持酷我和网易云平台，使用方法：/kw 歌名 或者 /wyy 歌名'))
        return

    elif message.display.strip() == '6':
        #以图搜图
        await app.send_message(group,MessageChain('本功能暂时关闭，如需技术支持，请联系管理员笙熙：2973918177'))
        return

    elif message.display.strip() == '9':
        #翻译
        await app.send_message(group,MessageChain('指令：/tra 目标语言 语句\n例：/tra en 你好\nen：英文，ch：中文'))
        return

    elif message.display.strip() == '10':
        #专业
        await app.send_message(group,MessageChain('请输入专业全称，全称如下'))
        await app.send_message(group,MessageChain(Image(path=f'./modules/专业.png')))
        return

    elif message.display.strip() == '5':
        #AI绘图
        await app.send_message(group,MessageChain('指令：/aip 描述\n例：/aip 一个漂亮的女孩，有着蓝色的头发和大眼睛\n当前仅支持动漫类型'))
        return

    elif message.display.strip() == '11' or message.display.strip() == '使用方法':
        # 使用方法
        await app.send_message(group,MessageChain(Image(path=f'./modules/方法.png')))
        return

    elif message.display.strip() == '12':
        # 关于
        await app.send_message(group,MessageChain(Image(path=f'./modules/关于.png')))
        await app.send_message(group,MessageChain('https://asxez.github.io'))
        return

    elif message.display.strip() == '/shutdown' and member.id == config.YOU_QQ:
        #关机
        await app.send_message(group,MessageChain('系统将在三秒后关闭，关闭后，需人为启动系统'))
        await asyncio.sleep(3.0)
        app.stop()
    else:
        return
