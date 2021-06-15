# encoding:utf-8
# 调用模块
import socket  
import time

addess = ('192.168.3.33', 2345)
BUF_SIZE = 1024

tcp_server = socket.socket()          # 创建socket
tcp_server.bind(addess)               # 为socket绑定IP地址与端口号
tcp_server.listen(3)                  # 客户端连接人数

while True:
      print("waiting for connection...")
      conn, addr = tcp_server.accept()    # 等待客户端连接
      print("...connected from:",addr)
      while True:
            data = conn.recv(BUF_SIZE)    # 接收的信息
            if not data:
                  break
            print("ok")
            inp = raw_input('>>:')
            conn.send(bytes(inp).encode('utf-8'))
tcp_server.close()
