from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel=Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def main(app:Ariadne, group:Group, message:MessageChain):
    if message.display.strip() == '工商管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/工商管理.png')))
    elif message.display.strip() == '财务管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/财务管理.png')))
    elif message.display.strip() == '国际经济与贸易':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/国际经济与贸易.png')))
    elif message.display.strip() == '物流管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/物流管理.png')))
    elif message.display.strip() == '旅游管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/旅游管理.png')))
    elif message.display.strip() == '汉语言文学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/汉语言文学.png')))
    elif message.display.strip() == '广播电视学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/广播电视学.png')))
    elif message.display.strip() == '音乐学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/音乐学.png')))
    elif message.display.strip() == '音乐表演':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/音乐表演.png')))
    elif message.display.strip() == '舞蹈表演':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/舞蹈表演.png')))
    elif message.display.strip() == '广播电视编导':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/广播电视编导.png')))
    elif message.display.strip() == '财务管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/财务管理.png')))
    elif message.display.strip() == '电子信息科学与技术':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/电子信息科学与技术.png')))
    elif message.display.strip() == '电子信息工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/电子信息工程.png')))
    elif message.display.strip() == '机械电子工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/机械电子工程.png')))
    elif message.display.strip() == '小学教育':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/小学教育.png')))
    elif message.display.strip() == '应用心理学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/应用心理学.png')))
    elif message.display.strip() == '学前教育':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/学前教育.png')))
    elif message.display.strip() == '社会工作':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/社会工作.png')))
    elif message.display.strip() == '法学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/法学.png')))
    elif message.display.strip() == '知识产权':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/知识产权.png')))
    elif message.display.strip() == '行政管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/行政管理.png')))
    elif message.display.strip() == '劳动与社会保障':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/劳动与社会保障.png')))
    elif message.display.strip() == '公共事业管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/公共事业管理.png')))
    elif message.display.strip() == '公共关系学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/公共关系学.png')))
    elif message.display.strip() == '英语':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/英语.png')))
    elif message.display.strip() == '日语':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/日语.png')))
    elif message.display.strip() == '汉语国际教育':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/汉语国际教育.png')))
    elif message.display.strip() == '物理学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/物理学.png')))
    elif message.display.strip() == '数学与应用数学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/数学与应用数学.png')))
    elif message.display.strip() == '计算机科学与技术':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/计算机科学与技术.png')))
    elif message.display.strip() == '数字媒体技术':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/数字媒体技术.png')))
    elif message.display.strip() == '软件工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/软件工程.png')))
    elif message.display.strip() == '数据科学与大数据技术':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/数据科学与大数据技术.png')))
    elif message.display.strip() == '信息与计算科学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/信息与计算科学.png')))
    elif message.display.strip() == '化学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/化学.png')))
    elif message.display.strip() == '应用化学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/应用化学.png')))
    elif message.display.strip() == '材料化学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/材料化学.png')))
    elif message.display.strip() == '制药工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/制药工程.png')))
    elif message.display.strip() == '美术学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/美术学.png')))
    elif message.display.strip() == '视觉传达设计':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/视觉传达设计.png')))
    elif message.display.strip() == '环境设计':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/环境设计.png')))
    elif message.display.strip() == '产品设计':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/产品设计.png')))
    elif message.display.strip() == '生物工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/生物工程.png')))
    elif message.display.strip() == '食品科学与工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/食品科学与工程.png')))
    elif message.display.strip() == '生物科学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/生物科学.png')))
    elif message.display.strip() == '农学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/农学.png')))
    elif message.display.strip() == '应用生物科学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/应用生物科学.png')))
    elif message.display.strip() == '茶学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/茶学.png')))
    elif message.display.strip() == '动植物检疫':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/动植物检疫.png')))
    elif message.display.strip() == '林学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/林学.png')))
    elif message.display.strip() == '环境工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/环境工程.png')))
    elif message.display.strip() == '工程管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/工程管理.png')))
    elif message.display.strip() == '汽车服务工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/汽车服务工程.png')))
    elif message.display.strip() == '建筑电气与智能化':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/建筑电气与智能化.png')))
    elif message.display.strip() == '工业工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/工业工程.png')))
    elif message.display.strip() == '质量管理工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/质量管理工程.png')))
    elif message.display.strip() == '食品质量与安全':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/食品质量与安全.png')))
    elif message.display.strip() == '安全工程':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/安全工程.png')))
    elif message.display.strip() == '体育教育':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/体育教育.png')))
    elif message.display.strip() == '社会体育指导与管理':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/社会体育指导与管理.png')))
    elif message.display.strip() == '康复治疗学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/康复治疗学.png')))
    elif message.display.strip() == '护理学':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/护理学.png')))
    elif message.display.strip() == '思想政治教育':
        await app.send_message(group,MessageChain(Image(path='./modules/data/school/思想政治教育.png')))
    else:
        return

