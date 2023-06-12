import re
import time
import uuid

from . import EdgeGPT

COOKIE_FILE_PATH = './modules/cookie.json'
CHATBOT = {}

token = ''
style = 'precise'

def getChatBot(token: str) -> tuple:
    global CHATBOT
    if token in CHATBOT:
        chatBot = CHATBOT[token]['chatBot']
        CHATBOT[token]['useTime'] = time.time()
    else:
        chatBot = EdgeGPT.Chatbot(COOKIE_FILE_PATH)
        token = str(uuid.uuid4())
        CHATBOT[token] = {}
        CHATBOT[token]['chatBot'] = chatBot
        CHATBOT[token]['useTime'] = time.time()
    return token, chatBot


def getStyleEnum(style: str) -> EdgeGPT.ConversationStyle:
    enum = EdgeGPT.ConversationStyle
    if style == 'balanced':
        enum = enum.balanced
    elif style == 'creative':
        enum = enum.creative
    elif style == 'precise':
        enum = enum.precise
    return enum


def getAnswer(data: dict) -> str:
    messages = data.get('item').get('messages')
    if 'text' in messages[1]:
        return messages[1].get('text')
    else:
        return messages[1].get('adaptiveCards')[0].get('body')[0].get('text')


def filterAnswer(answer: str) -> str:
    answer = re.sub(r'\[\^.*?\^]', '', answer)
    answer = answer.rstrip()
    return answer


def needReset(data: dict, answer: str) -> bool:
    maxTimes = data.get('item').get('throttling').get('maxNumUserMessagesInConversation')
    nowTimes = data.get('item').get('throttling').get('numUserMessagesInConversation')
    errorAnswers = ['I’m still learning', '我还在学习']
    if [errorAnswer for errorAnswer in errorAnswers if errorAnswer in answer]:
        return True
    elif nowTimes == maxTimes:
        return True
    return False

# 检查token会让整体响应变慢，直接不用就行
# async def checkToken() -> None:
#     global CHATBOT
#     while True:
#         for token in CHATBOT.copy():
#             if time.time() - CHATBOT[token]['useTime'] > 5 * 60:
#                 await CHATBOT[token]['chatBot'].close()
#                 del CHATBOT[token]
#         await asyncio.sleep(60)


async def api(question):
    ## 获取参数，这里可以修改
    global token
    global style

    token, chatBot = getChatBot(token)
    data = await chatBot.ask(question, conversation_style=getStyleEnum(style))

    if data.get('item').get('result').get('value') == 'Throttled':
        print('已上限,24小时后尝试')

    answer = getAnswer(data)
    answer = filterAnswer(answer)

    if needReset(data, answer):
        await chatBot.reset()
    return answer


async def writer(question):
    prompt = "please help me,you only answer my question"
    #await api_weather(prompt)
    response=await api(question)
    return str(response)

'''
async def reset():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        "--proxy",
        help="Proxy URL (e.g. socks5://127.0.0.1:1080)",
        type=str,
    )
    parser.add_argument(
        "--cookie-file",
        type=str,
        default="cookie.json",
        required=False,
        help="needed if environment variable COOKIE_FILE is not set",
    )
    args=parser.parse_args()
    bot=EdgeGPT.Chatbot(proxy=args.proxy)
    await bot.reset()
'''
'''
if __name__ == '__main__':
    #token = ""  # 连续对话使用的toke，不用修改，默认开启，如果想要关闭，注释140行即可 （连续对话有限制，目前是20次对话）
    style = 'precise'  # bing的对话有三种模式  1.'balanced',  2. 'creative', 3.'precise' 必须选择其中一种
    question = "我是笙熙"
    asyncio.run(writer(question))
'''

