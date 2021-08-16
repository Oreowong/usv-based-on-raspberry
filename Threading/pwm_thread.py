# encoding:UTF-8
#修改无人船的电机控制程序来控制四电机浮标

import serial # 导入串口包
import time   # 导入时间包
import RPi.GPIO as GPIO  #引入RPi.GPIO库函数命名为GPIO
import threading

from serial_thread import Serialthread

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)        #将GPIO编程方式设置为BCM模式,
# 输出模式
#修改PWM输出个数，从而控制四电机浮标

#电机右1
GPIO.setup(4, GPIO.OUT)       
MotorR1 = GPIO.PWM(4, 50)
MotorR1.start(7.1)
#电机u左1
GPIO.setup(5, GPIO.OUT)        
MotorL1 = GPIO.PWM(5, 50)
MotorL1.start(7.1)
#电机右2
GPIO.setup(6, GPIO.OUT)       
MotorR2 = GPIO.PWM(6, 50)
MotorR2.start(7.1)
#电机左2
GPIO.setup(7, GPIO.OUT)        
MotorL2 = GPIO.PWM(7, 50)
MotorL2.start(7.1)


class Pwmthread:
    def __init__(self, ser_thread): 
        self.r = ser_thread
        self.working = False
        self.iniVariable()  #初始化变量
    def iniVariable(self):    
        self.Direct =  " "
    #接收数据
    def receive(self):        
        while self.working:
            time.sleep(0.01)
            #休眠一个微小的时间，可以避免无谓的CPU占用
            data = self.r.Rev_data
            if data == 'w':
                    MotorL1.ChangeDutyCycle(6)
                    MotorR1.ChangeDutyCycle(6)
                    MotorL2.ChangeDutyCycle(6)
                    MotorR2.ChangeDutyCycle(6)                   
                    self.Direct = "Go ahead!"
            elif data == 'a':
                    MotorL1.ChangeDutyCycle(7.1)
                    MotorR1.ChangeDutyCycle(6)
                    MotorL2.ChangeDutyCycle(6)
                    MotorR2.ChangeDutyCycle(6)                     
                    self.Direct = "Turn left"
            elif data == 's':
                    MotorL1.ChangeDutyCycle(8)
                    MotorR1.ChangeDutyCycle(8)
                    MotorL2.ChangeDutyCycle(8)
                    MotorR2.ChangeDutyCycle(8) 
                    self.Direct = "Go back!"
            elif data == 'd':
                    MotorL1.ChangeDutyCycle(6)
                    MotorR1.ChangeDutyCycle(7.1) 
                    MotorL2.ChangeDutyCycle(6)
                    MotorR2.ChangeDutyCycle(6)                                      
                    self.Direct = "Turn right!"
            elif data == 'x':
                    MotorL1.ChangeDutyCycle(7.1)
                    MotorR1.ChangeDutyCycle(7.1)
                    MotorL2.ChangeDutyCycle(7.1)
                    MotorR2.ChangeDutyCycle(7.1)                  
                    self.Direct = "STOP!"
            else:
                    self.Direct = "No command!"
    #开始工作
    def start(self):
        #开始数据读取线程
        t = threading.Thread(target=self.receive)
        #将当前线程设为子线程t的守护线程，这样一来，当前线程结束时会强制子线程结束
        t.setDaemon(True)
        self.working = True
        t.start()
    #停止工作
    def stop(self):
        self.working = False
        
#如果本文件被引用则面函数不被执行
if __name__=="__main__":
    s = Serialthread()
    s.start()
    p = Pwmthread(s)
    p.start()

    while True:
        time.sleep(1)
        s.send(p.Direct)
        print(p.Direct)
        
