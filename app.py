from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello ปิยกร เลขที่4"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/hi')
@app.route('/hello')
def hi():
    return "นี้เป็นข้อความอัตโนมัติ กรุณารอสักครู่"
    if msgType == "text":
        msg = str(event["message"]["text"])
        if msg == "สวัสดี" :      
            replyObj = TextSendMessage(text="นี้เป็นข้อความอัตโนมัติ กรุณารอสักครู่")
            line_bot_api.reply_message(rtoken, replyObj)
        elif msg == "สวัสดีครับ" :      
            replyObj = TextSendMessage(text="นี้เป็นข้อความอัตโนมัติ กรุณารอสักครู่")
            line_bot_api.reply_message(rtoken, replyObj)
        elif msg == "สวัสดีค่ะ" :      
            replyObj = TextSendMessage(text="นี้เป็นข้อความอัตโนมัติ กรุณารอสักครู่")
            line_bot_api.reply_message(rtoken, replyObj)
    
        else :  
            headers = request.headers
            json_headers = ({k:v for k, v in headers.items()})
            json_headers.update({'Host':'bots.dialogflow.com'})
            url = "https://bots.dialogflow.com/line/502043e2-a86c-437b-85a8-0f9f3b389631/webhook"
            requests.post(url,data=json_line, headers=json_headers)
    elif msgType == "image":
        try:
            message_content = line_bot_api.get_message_content(event['message']['id'])
            i = Image.open(BytesIO(message_content.content))
            filename = event['message']['id'] + '.jpg'
            i.save(UPLOAD_FOLDER + filename)
            process_file(os.path.join(UPLOAD_FOLDER, filename), filename)

            url = request.url_root + DOWNLOAD_FOLDER + filename
            
            line_bot_api.reply_message(
                rtoken, [
                    TextSendMessage(text='Object detection result:'),
                    ImageSendMessage(url,url)
                ])    
    
        except:
            message = TextSendMessage(text="เกิดข้อผิดพลาด กรุณาส่งใหม่อีกครั้ง")
            line_bot_api.reply_message(event.reply_token, message)

            return 0

    else:
        sk_id = np.random.randint(1,17)
        replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
        line_bot_api.reply_message(rtoken, replyObj)
    return ''

if __name__ == '__main__':
    app.run()

if __name__ == "__main__":
    app.run(debug=False)
