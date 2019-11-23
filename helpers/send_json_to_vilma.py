#This file will send a json object to vilma

import config
import socket
import json

def send_json_to_vilma(json_object):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((config.vilma_host,config.vilma_port))


    str_data = json.dumps(json_object)

    s.sendall(str_data.encode())


    ret = s.recv(2048)

    return ret.decode()

