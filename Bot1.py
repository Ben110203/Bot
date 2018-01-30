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

app = Flask(__name__)

# Replace by your channel secret and access token from Line Developers console -> Channel settings.
LINE_CHANNEL_SECRET = '519c10e98f832890d3ce45a28d42a37f'
LINE_CHANNEL_ACCESS_TOKEN = 'aiL6gJ0FSxqm/EdwDPKA9n9BmTTWEaJbaKqUjayZaOm3nYwEwBCXECsTKEQQGTKLxxoL8u/VInK27Ju/glylBpQ5p+ezqQoaCF76Xah3PhWa+TmTUvbOt4VxvMr+9hC+PPzApEnRufogOPdVX+rfdQdB04t89/1O/w1cDnyilFU='
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
    # Replace the text by what you want to say
    line_bot_api.reply_message(
        event.reply_token,
  #      ImageSendMessage( original_content_url='https://addons.cdn.mozilla.net/user-media/addon_icons/824/824288-64.png?modified=1516050890', preview_image_url='https://addons.cdn.mozilla.net/user-media/addon_icons/824/824288-64.png?modified=1516050890'))
        TextSendMessage(text=event.message.text))
def reply(text):
    if text == "剪刀":
        return "石頭"
    elif text == "石頭":
        return "布"
    elif text == "布":
        return "剪刀"
    else:
        return "Hello world"

if __name__ == "__main__":
    app.run()
