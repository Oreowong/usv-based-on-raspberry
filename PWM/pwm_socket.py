# encoding:UTF-8
import serial # 导入串口包
import time   # 导入时间包
import RPi.GPIO as GPIO     #引入RPi.GPIO库函数命名为GPIO
import socket

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)                    #将GPIO编程方式设置为BOARD模式
# 输出模式
GPIO.setup(11, GPIO.OUT)                    #将GPIO引脚11设置为输出引脚
GPIO.setup(12, GPIO.OUT)                    #将GPIO引脚12设置为输出引脚
MotorL = GPIO.PWM(11, 50)
MotorL.start(7)
MotorR = GPIO.PWM(12, 50)
MotorR.start(7)

BUF_SIZE = 1024
addess = ('192.168.3.33', 2345)
tcp_server = socket.socket()                 # 创建socket
tcp_server.bind(addess)                      # 为socket绑定IP地址与端口号
tcp_server.listen(3) 

def pwm_socket():    
    while True:
        print("Waiting for the connection...")
        conn, addr = tcp_server.accept()    # 等待客户端连接
        print("...connected from:",addr)
        conn.send(bytes("Please input the command!").encode('utf-8'))
        while True:
            data = conn.recv(BUF_SIZE)    # 接收的信息
            if not data:
                break
            elif data == 'w':
                MotorL.ChangeDutyCycle(8)
                MotorR.ChangeDutyCycle(8)
                conn.send(bytes("Go ahead!").encode('utf-8'))
            elif data == "a":
                MotorL.ChangeDutyCycle(7)
                MotorR.ChangeDutyCycle(8)
                conn.send(bytes("Turn left").encode('utf-8'))
            elif data == "s":
                MotorL.ChangeDutyCycle(6)
                MotorR.ChangeDutyCycle(6)
                conn.send(bytes("Go back!").encode('utf-8'))
            elif data == "d":
                MotorL.ChangeDutyCycle(8)
                MotorR.ChangeDutyCycle(6)                   
                conn.send(bytes("Turn right!").encode('utf-8'))  
            elif data == "x":
                MotorL.stop()
                MotorR.stop()
                conn.send(bytes("STOP!").encode('utf-8'))
            else:
                conn.send(bytes("Wrong command!").encode('utf-8'))
            time.sleep(0.1) # 延时0.1秒，免得CPU出问题
