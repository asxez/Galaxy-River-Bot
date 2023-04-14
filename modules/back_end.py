import re

import config
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Friend
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel=Channel.current()

@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def h(app:Ariadne, friend:Friend, message:MessageChain,):
    if friend.id == config.YOU_QQ:
        if message.display.strip().split(' ')[0] == '/s':
            text=re.findall('^/s\s(.*)',message.display.strip(),re.S)[0]
            await app.send_group_message(config.group_id,MessageChain(text))
        else:
            return
    else:
        await app.send_message(friend,MessageChain('无权限'))
