"""
配置文件
请自行配置
"""

#不懂的可以不用管
http="http://localhost:8080"
ws="ws://localhost:8080"


#机器人qq
BOT_QQ: int

#openai的key
OPENAI_KEY=""

#群违禁词，我这里设定的大于等于两个则撤回，你们自己在manage模块66行里改
KEYWORD=[]

#管理员
MANAGE_PEOPLE=[]

#系统管理员 （int类型）
#可以自己改list类型,注意模块中的地方，你要自己改一个遍历什么的，或者 a in [],建议用后者
YOU_QQ: int
#mirai
verifyKey=''

#AI绘图key
#地址：http://flagstudio.baai.ac.cn/document#1
AI_IMAGE_KEY=""

#高德key
GD_KEY=''

#所需发送的群号
#我只用在一个群，所以是int类型，你们可以自改list类型，这个改成list类型了也要改模块中的部分代码
group_id: int

#定时笑话，地址：https://www.mxnzp.com/
SMILE_APPID=''
SMILE_APPSECRET=''



"""
其余的配置在模块文件里
"""

"""
我用的python版本是3.10.6
建议使用3.10及以上，至少要3.4，支持异步库的
"""
