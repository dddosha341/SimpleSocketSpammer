import sys
import argparse
import socket
import time
import random

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def CreateParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--ip', default='127.0.0.1')
    parser.add_argument('-p','--port', default=str(80))
    return parser
def GenerateRandomWord() -> str:
    data = ''
    for i in range(0,20):
        int = round(10,90)
        data+=chr(int)
    return data
def RandomTime() -> float:
    millisecondsRandom = round(100,200)
    return float(millisecondsRandom/1000)
if __name__ == '__main__':
    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:])
    port = int(namespace.port)
    clientSocket.connect((namespace.ip,(int(namespace.port))))
    print('GOOD CONNECT')
    while True:
        data = GenerateRandomWord()
        timeSleep = RandomTime()
        try:
             clientSocket.send(data.encode())
             print('SENDED')
        except:
            print('NOT SENDED! ERROR!')
            continue
        time.sleep(timeSleep)
    
