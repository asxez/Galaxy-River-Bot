<div align="center">

# Galaxy-River-Bot
🐔一个以 [Graia Ariadne](https://github.com/GraiaProject/Ariadne) 框架为基础的 QQ 机器人🐔

</div>

# 本机功能
1. ChatGPT  API版（无上下文）（需魔法） /gpt
2. New Bing （有上下文）（需魔法） /bing
3. AI绘画 /aip
4. 随机动漫图片
5. 基本翻译
6. 人工图库（我亲手挑选的）
7. 音乐（目前支持酷我和网易云）/kw /wyy
8. 随机一言
9. 群违规词检测
10. 入群申请检测与审核
11. 定时推送实况天气
12. 定时发送笑话段子（时间设在14：20，因为大家才睡了午觉没啥精神）
13. 星期四定时发送疯狂星期四文案
14. /kick /ma /uma /mo /umo /tra /shutdown
15. 控制端后门

    more……

# 食用方法🐔
1. 下载依赖：pip install -r requirements.txt
2. 终端运行：python bot.py   ----注意：运行的前提是你已经启动了mcl并已登录


# 注意！
1. 本机仅为学校新生群管理所需进行开发，主要是管理QQ群，针对我们的需要，很有可能随时大改，不建议clone
2. New Bing 的cookie获取后粘贴在modules目录下的cookie.json文件中，获取方法请到我的博客文章中查看。
[博客链接](https://asxez.github.io/2023/04/12/%E5%9F%BA%E4%BA%8Emirai%E5%92%8Cgraia%E7%9A%84QQ%E6%9C%BA%E5%99%A8%E4%BA%BA/#%E6%B3%A8%E6%84%8F)

# 鸣谢

> 这些项目也很棒, 可以去他们的项目主页看看, 点个 Star 鼓励他们的开发工作吧

感谢
- [`mirai`](https://github.com/mamoe/mirai) & [`mirai-console`](https://github.com/mamoe/mirai-console): 一个在全平台下运行，提供 QQ Android 和 TIM PC 协议支持的高效率机器人框架
- [`mirai-api-http`](https://github.com/project-mirai/mirai-api-http): 为本项目提供与 mirai 交互方式的 mirai-console 插件
- [`GraiaProject`](https://github.com/GraiaProject) 带来的这些项目:
- [`Broadcast Control`](https://github.com/GraiaProject/BroadcastControl): 高性能, 高可扩展性，设计简洁，基于 asyncio 的事件系统
- [`Ariadne`](https://github.com/GraiaProject/Ariadne): 一个设计精巧, 协议实现完备的, 基于 mirai-api-http v2 的即时聊天软件自动化框架
- [`Saya`](https://github.com/GraiaProject/Saya):简洁的模块管理系统
- [`Scheduler`](https://github.com/GraiaProject/Scheduler): 简洁的基于 `asyncio` 的定时任务实现
- [`EdgeGPT`](https://github.com/acheong08/EdgeGPT) :new bing逆向工程

# 许可证
MIT
