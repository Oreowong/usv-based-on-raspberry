# encoding:utf-8

# 调用模块
import socket  
 
addess = ('192.168.3.35', 2345) 
client  = socket.socket()		# 创建socket
client.connect(addess)			# 连接服务端IP地址和端口号

while True:
	data = input('>>:')
	#if not data:break
	client.send(bytes(data).encode('utf-8'))    # bytes编码后发送信息
	recv_data = client.recv(1024)
	if not recv_data:break
	print(str(recv_data).encode('utf-8'))    #str解码后打印出来
client.close()
