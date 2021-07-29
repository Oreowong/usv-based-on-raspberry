# encoding:UTF-8
import serial # 导入串口包
import time   # 导入时间包
import RPi.GPIO as GPIO  #引入RPi.GPIO库函数命名为GPIO
import threading

from serial_thread import Serialthread

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)        #将GPIO编程方式设置为BOARD模式
# 输出模式
#修改PWM输出个数，从而控制四电机浮标
GPIO.setup(11, GPIO.OUT)        #将GPIO引脚11设置为输出引脚
MotorR = GPIO.PWM(11, 50)
MotorR.start(7.1)
GPIO.setup(12, GPIO.OUT)        #将GPIO引脚12设置为输出引脚
MotorL = GPIO.PWM(12, 50)
MotorL.start(7.1)

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
                    MotorL.ChangeDutyCycle(6)
                    MotorR.ChangeDutyCycle(6)
                    self.Direct = "Go ahead!"
            elif data == 'a':
                    MotorL.ChangeDutyCycle(7.1)
                    MotorR.ChangeDutyCycle(6)
                    self.Direct = "Turn left"
            elif data == 's':
                    MotorL.ChangeDutyCycle(8)
                    MotorR.ChangeDutyCycle(8)
                    self.Direct = "Go back!"
            elif data == 'd':
                    MotorL.ChangeDutyCycle(6)
                    MotorR.ChangeDutyCycle(7.1)                   
                    self.Direct = "Turn right!"
            elif data == 'x':
                    MotorL.ChangeDutyCycle(7.1)
                    MotorR.ChangeDutyCycle(7.1)
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
        
