import sys
import argparse
import socket
import time
import random

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--ip', default='127.0.0.1')
    parser.add_argument('-p','--port', default=str(80))
    parser.add_argument('-t','--time', default=str(0))
    return parser
def generateRandomWord() -> str:
    data = ''
    for i in range(0,20):
        int = round(10,90)
        data+=chr(int)
    return data
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    port = int(namespace.port)
    clientSocket.connect((namespace.ip,(int(namespace.port))))
    timeSleep = float(namespace.time)
    print('GOOD CONNECT')
    while True:
        data = generateRandomWord()
        try:
             clientSocket.send(data.encode())
             print('SENDED')
        except:
            print('ERROR!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!')
            continue
        time.sleep(timeSleep)
    