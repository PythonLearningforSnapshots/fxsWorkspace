import socket
import time

#在python3.x，socket的流的类型是bytes，而不是str，在python2.x，str和bytes是不加区分的，所以使用中有所不同
def socket_demo():
    #初始化套接字类，AF_INET代表IPV4，SOCK_STREAM代表TCP/IP套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #绑定主机资源，参数为元组（address,port）
    server.bind(('localhost', 8080))
    #开始TCP监听
    server.listen(5)
    n = 0

    while True:
        #被动接受TCP客户的连接,(阻塞式)等待连接的到来
        conn, addr  = server.accept()
        #收到信息
        msg = conn.recv(1024)
        print(str(msg,encoding = "utf-8"))
        #发送信息
        conn.send(b'HTTP/1.1 200 OK \r\n\r\n')
        time.sleep(1)
        n += 1
        conn.send(bytes('hello xiaoshi{0}'.format(n),encoding = "utf-8"))
        #关闭连接
        conn.close()


def main():
    socket_demo()

main()