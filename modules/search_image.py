from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import *
from graia.ariadne.message.parser.twilight import Twilight, FullMatch, ElementMatch, ElementResult
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from saucenao_api import AIOSauceNao
from saucenao_api.errors import SauceNaoApiError

channel = Channel.current()

channel.name("Saucenao")
channel.description("以图搜图")
channel.author("asxe")

apikey = "" # 请输你自己的

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        inline_dispatchers=[
            Twilight(
                FullMatch("以图搜图"),
                FullMatch("\n", optional=True),
                "img" @ ElementMatch(Image, optional=True),
            ),
        ],
    )
)
async def saucenao(app: Ariadne, group: Group, member: Member, img: ElementResult, source: Source):
    await app.send_group_message(group, MessageChain("正在搜索，请稍后"), quote=source.id)
    async with AIOSauceNao(apikey, numres=3) as snao:
        try:
            results = await snao.from_url(img.result.display.strip())
        except SauceNaoApiError as e:
            await app.send_message(group, MessageChain("搜索失败desu"))
            return

    fwd_nodeList = []
    for results in results.results:
        if len(results.urls) == 0:
            continue
        urls = "\n".join(results.urls)
        fwd_nodeList.append(
            ForwardNode(
                target=app.account,
                time=datetime.now(),
                message=MessageChain(
                    f"相似度：{results.similarity}%\n标题：{results.title}\n节点名：{results.index_name}\n链接：{urls}"
                )))

    if len(fwd_nodeList) == 0:
        await app.send_message(group, MessageChain("未找到有价值的数据"), quote=source.id)
    else:
        await app.send_message(group, MessageChain(Forward(nodeList=fwd_nodeList)))
