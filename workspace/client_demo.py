import socket

def client_demo():
    #初始化
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #建立连接
    client.connect(('127.0.0.1', 8080))
    #发送消息
    client.send('hello'.encode('utf-8'))
    #接受消息
    msg = client.recv(1024)
    while msg:
        print(str(msg,'utf8'))
        msg = client.recv(1024)

    client.close()

def main():
    for i in range(10):
        client_demo()

main()