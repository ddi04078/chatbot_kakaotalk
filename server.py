from flask import Flask, request, jsonify
from chatterbox import Chatter
from chatterbox.response import Text, Keyboard, MessageButton


app = Flask(__name__)
chatter = Chatter()


@chatter.base(name='홈')
def home_keyboard():
    home_buttons = ['과사무실 전화번호', '소프트웨어융합대학 홈페이지', '문의하기']
    return Keyboard(home_buttons)

@chatter.rule(action='과사무실 전화번호', src='홈', dest='홈')
def intro(data):
    message = '안녕하세요 소프트웨어융합대학입니다.',
    message = '029104790'
    return Text(message) + chatter.home()

@chatter.rule(action='소프트웨어융합대학 홈페이지', src='홈', dest='홈')
def web(data):
    text = Text('자세한 정보를 보고싶으면 사이트로 이동해주세요!')
    msg_button = MessageButton(label='이동하기',
                               url='https://cs.kookmin.ac.kr')
    keyboard = chatter.home()
    return text + msg_button + keyboard

@app.route('/keyboard', methods=['GET'])
def keyboard():
    return jsonify(chatter.home())

@app.route('/message', methods=['POST'])
def message():
    return jsonify(chatter.route(request.json))


if __name__ == '__main__':
    app.run(debug=True)
