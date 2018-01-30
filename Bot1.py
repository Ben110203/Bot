rom flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage
)

import random

replylist = ["剪刀","石頭","布"]

app = Flask(__name__)

# Replace by your channel secret and access token from Line Developers console -> Channel settings.
LINE_CHANNEL_SECRET = 'd7cd6ac3a091291e21bd679b8bda9d54'
LINE_CHANNEL_ACCESS_TOKEN = 'r+r82dIkwmOVnI43ehvHJaQbjUQl21tNGcoruT7aP1HxJSmeP1QTTALK3mkKjc+pxxoL8u/VInK27Ju/glylBpQ5p+ezqQoaCF76Xah3PhUm139iyRFG1wouMgff+e5H96nNfTQK0hU8CY31tq30/wdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text  in replylist:
        if  event.message.text== "剪刀" or "石頭" or "布":
            t = random.sample(replylist, 1)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=t))
            if event.message.text == t:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="平手!"))
            elif (event.message.text=="剪刀"and t == "石頭") or (event.message.text=="石頭"and t == "布") or (event.message.text=="剪刀"and t == "石頭"):
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="你輸了！"))
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="你贏了！"))

    else:
        if event.message.text in replylist:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Hi"))

def reply(text):


def WinOrLose(text):

if __name__ == "__main__":
    app.run()
