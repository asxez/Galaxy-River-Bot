import config
import random
import requests
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.scheduler import timers
from graia.scheduler.saya.schema import SchedulerSchema

channel = Channel.current()

api_weather = 'https://restapi.amap.com/v3/weather/weatherInfo'
data_weather = {
    'key':config.GD_KEY,
    'city':'511502',
    'extensions':'base',
    'output':'JSON'
}

api_smile = 'https://www.mxnzp.com/api/jokes/list'

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

@channel.use(SchedulerSchema(timer=timers.crontabify('30 7 * * *')))
async def morning(app:Ariadne):
    res = requests.get(api_weather, params=data_weather, headers=header).json()
    if res:
        try:
            if res.get('status') == '1':
                if res.get('infocode') == '10000':
                    weather = res.get('lives')[0].get('weather')
                    temperature = res.get('lives')[0].get('temperature')
                    if weather == '晴':
                        await app.send_group_message(config.group_id,MessageChain(f"实况天气\n时间：北京时间7点30分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}"))
                        return
                    else:
                        await app.send_group_message(config.group_id, MessageChain(f"实况天气\n时间：北京时间7点30分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}\n请注意添加衣物"))
                        return
                else:
                    await app.send_group_message(config.group_id,MessageChain('状态错误，获取天气信息失败'))
                    return
            else:
                await app.send_group_message(config.group_id,MessageChain('请求失败，获取天气信息失败'))
                return
        except:
            return
    else:
        await app.send_group_message(config.group_id,MessageChain('请求失败'))
        return

@channel.use(SchedulerSchema(timer=timers.crontabify('50 13 * * *')))
async def afternoon(app:Ariadne):
    res = requests.get(api_weather, params=data_weather, headers=header).json()
    if res:
        try:
            if res.get('status') == '1':
                if res.get('infocode') == '10000':
                    weather = res.get('lives')[0].get('weather')
                    temperature = res.get('lives')[0].get('temperature')
                    if weather == '晴':
                        await app.send_group_message(config.group_id,MessageChain(f"实况天气\n时间：北京时间13点50分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}"))
                        return
                    else:
                        await app.send_group_message(config.group_id, MessageChain(f"实况天气\n时间：北京时间13点50分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}\n请注意添加衣物"))
                        return
                else:
                    await app.send_group_message(config.group_id,MessageChain('状态错误，获取天气信息失败'))
                    return
            else:
                await app.send_group_message(config.group_id,MessageChain('请求失败，获取天气信息失败'))
                return
        except:
            return
    else:
        await app.send_group_message(config.group_id,MessageChain('请求失败'))
        return

@channel.use(SchedulerSchema(timer=timers.crontabify('30 18 * * *')))
async def night(app:Ariadne):
    res = requests.get(api_weather, params=data_weather, headers=header).json()
    if res:
        try:
            if res.get('status') == '1':
                if res.get('infocode') == '10000':
                    weather = res.get('lives')[0].get('weather')
                    temperature = res.get('lives')[0].get('temperature')
                    if weather == '晴':
                        await app.send_group_message(config.group_id,MessageChain(f"实况天气\n时间：北京时间18点30分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}"))
                        return
                    else:
                        await app.send_group_message(config.group_id, MessageChain(f"实况天气\n时间：北京时间18点30分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}\n请注意添加衣物"))
                        return
                else:
                    await app.send_group_message(config.group_id,MessageChain('状态错误，获取天气信息失败'))
                    return
            else:
                await app.send_group_message(config.group_id,MessageChain('请求失败，获取天气信息失败'))
                return
        except:
            return
    else:
        await app.send_group_message(config.group_id,MessageChain('请求失败'))
        return

"""
@channel.use(SchedulerSchema(timer=timers.crontabify('56 21 * * *')))
async def morning(app:Ariadne):
    res = requests.get(api_weather,params=data_weather,headers=header).json()
    if res:
        try:
            if res.get('status') == '1':
                if res.get('infocode') == '10000':
                    weather = res.get('lives')[0].get('weather')
                    temperature = res.get('lives')[0].get('temperature')
                    if weather == '晴':
                        await app.send_group_message(,MessageChain(f"实况天气\n时间：北京时间7点30分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}"))
                        return
                    else:
                        await app.send_group_message(, MessageChain(f"实况天气\n时间：北京时间7点30分\n位置：宜宾市翠屏区\n天气：{weather}\n温度：{temperature}\n请注意添加衣物"))
                        return
                else:
                    await app.send_group_message(,MessageChain('状态错误，获取天气信息失败'))
                    return
            else:
                await app.send_group_message(,MessageChain('请求失败，获取天气信息失败'))
                return
        except:
            return
    else:
        await app.send_group_message(,MessageChain('请求失败'))
        return
"""

@channel.use(SchedulerSchema(timer=timers.crontabify('20 14 * * *')))
async def smile_aft(app:Ariadne):
    """
    定时笑话
    :param app:
    :return:
    """
    page = random.randint(1, 8700)
    index = random.randint(1, 9)
    data_smile = {
        'page':int(page),
        'app_id':config.SMILE_APPID,
        'app_secret':config.SMILE_APPSECRET
    }
    res = requests.get(api_smile,params=data_smile,headers=header).json()
    if res:
        try:
            if res.get('code') == 1:
                text=res.get('data').get('list')[index].get('content')
                await app.send_group_message(config.group_id,MessageChain(f'当前时间：14:20\n{text}'))
                return
            else:
                return
        except:
            return
    else:
        return
