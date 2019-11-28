from flask import Flask,request,make_response
import sys

sys.path.append("./config")
sys.path.append("./helpers")

import config
from send_json_to_vilma import send_json_to_vilma
app = Flask(__name__)


@app.route('/api/v1/command',methods=["POST","GET","OPTIONS"])
def v1_command():
    if request.method == "GET":
        return "Use Post Methods to send & receive details!"
    elif request.method == "POST":
        ret = send_json_to_vilma(request.get_json())
        resp = make_response(ret)
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        resp.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return resp
    elif request.method == "OPTIONS":
        resp = make_response('{"code": 1, "message": "Status Ok!"}')
        resp.headers.add('Access-Control-Allow-Origin', '*')
        resp.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        resp.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return resp

    else:
        return "Error: Unouthorized Access"




if __name__ == '__main__':
    app.run(host= '0.0.0.0')
