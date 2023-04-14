import asyncio
import re

import config
import jieba
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, MessageEvent, ActiveGroupMessage, Source
from graia.ariadne.event.mirai import MemberJoinRequestEvent
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import ContainKeyword
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel=Channel.current()

keywords=config.KEYWORD
manage_people=config.MANAGE_PEOPLE
my_qq=config.YOU_QQ
me_id=[]

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def kick_members(app:Ariadne, group:Group, message:MessageChain, member:Member):
    """
    踢出指定成员
    :param app:
    :param group:
    :param message:
    :param member:
    :return:
    """
    if member.id in manage_people:
        if ContainKeyword('/kick') and message.display.strip().split(' ')[0]:
            try:
                qq = re.findall('^/kick\s@(\d+)',message.display.strip(),re.S)[0]
                if 7 < len(qq) <= 10:
                    await app.kick_member(group,int(qq))
                    await app.send_message(group,MessageChain(f'{qq}已被踢出'))
                    return
                else:
                    await app.send_message(group,MessageChain('请正确艾特要被踢出的对象'))
                    return
            except:
                return
        else:
            return
    else:
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def recall(app:Ariadne, message:MessageChain, event:MessageEvent):
    """
    违规撤回
    :param app:
    :param message:
    :param event:
    :return:
    """
    ls = jieba.lcut(message.display.strip())
    count = 0
    for every_keyword in ls:
        if every_keyword in keywords:
            count = count+1
        else:
            pass
    if count >= 2:
        await asyncio.sleep(1.0)
        await app.recall_message(event)
        count=0
    else:
        return

"""
撤回自己消息
"""
@channel.use(ListenerSchema(listening_events=[ActiveGroupMessage]))
async def get_id(app:Ariadne, event:Source):
    if app.account:
        me_id.append(event.id)
    else:
        pass
    if len(me_id) >= 20:
        del me_id[0]
    else:
        pass
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def recall_me(app:Ariadne, message:MessageChain, member:Member, group:Group):
    if message.display.strip().split(' ')[0] == '/reme' and member.id == my_qq:
        await app.recall_message(me_id[-1],group)
    else:
        return

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def mute(app:Ariadne, member:Member, group:Group, message:MessageChain):
    """
    禁言系统
    :param app:
    :param member:
    :param group:
    :param message:
    :return:
    """
    if member.id in manage_people:
        if ContainKeyword('/ma') and message.display.strip() == '/ma':
            await app.send_message(group,MessageChain('已开启全体禁言'))
            await app.mute_all(group)
            return
        #开启全体禁言

        elif ContainKeyword('/mo') and message.display.strip().split(' ')[0] == '/mo':
            try:
                qq = re.findall('^/mo\s@(\d+).*?',message.display.strip(),re.S)[0]
                mute_time = message.display.strip().split(' ')[2]
                if 7 < len(qq) <= 10:
                    await app.mute_member(group,int(qq),int(mute_time)*60)
                    await app.send_message(group,MessageChain(f'{qq}已被禁言'))
                    return
                else:
                    await app.send_message(group,MessageChain('请正确输入指令'))
                    return
            except:
                return
        #禁言成员

        elif ContainKeyword('/uma') and message.display.strip() == '/uma':
            await app.unmute_all(group)
            await app.send_message(group,MessageChain('全体禁言已解除'))
            return
        #解除全体禁言

        elif ContainKeyword('/umo') and message.display.strip().split(' ')[0] == '/umo':
            try:
                qq = re.findall('^/umo\s@(\d+)',message.display.strip(),re.S)[0]
                if 7 < len(qq) <=10:
                    await app.unmute_member(group,int(qq))
                    await app.send_message(group,MessageChain(f'{qq}已被解除禁言'))
                    return
                else:
                    await app.send_message(group,MessageChain('请正确输入指令'))
                    return
            except:
                return
        #解除成员禁言

        else:
            return
    else:
        return

@channel.use(ListenerSchema(listening_events=[MemberJoinRequestEvent]))
async def request_join(app:Ariadne, event:MemberJoinRequestEvent):
    """
    加群申请处理
    :param app:
    :param event:
    :return:
    """
    if event.supplicant:
        profile = await app.get_user_profile(event.supplicant)
        if profile.level >= 3:
            await event.accept('欢迎入群！群里输入”菜单“即可使用本机')
        else:
            await event.reject()
    else:
        return
