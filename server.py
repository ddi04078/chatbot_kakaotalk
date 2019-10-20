import os
from flask import Flask, request, jsonify
 
 
 
app = Flask(__name__)
 
 
 
@app.route('/keyboard')
def Keyboard():
 
    dataSend = {
        "type" : "buttons",
        "buttons" : ["start", "help"]
    }
 
    return jsonify(dataSend)
 
 
 
@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']
 
    if content == u"start":
        dataSend = {
            "message": {
                "text": "start Kakaotalk Plus friend automatic response"
            }
        }
    elif content == u"help":
        dataSend = {
            "message": {
                "text": "KMU CS call : 02-910-****"
            }
        }
    return jsonify(dataSend)
 
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 2468)
