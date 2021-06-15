# encoding:UTF-8
import serial # 导入串口包
import time   # 导入时间包
import threading

class Config:
    # 端口号
    serialPort = '/dev/ttyUSB1' 
    # 波特率 
    baudRate = 9600 

class Serialthread:
    def __init__(self): 
        self.port = serial.Serial(Config.serialPort, Config.baudRate,timeout = 0)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()
        self.working = False
        self.iniVariable()#初始化变量
    #打开
    def open(self):
        if not self.port.isOpen():
            self.port.open()
    #关闭
    def close(self):
        self.port.close()
    #初始化解析相关的变量
    def iniVariable(self):    
        self.Rev_data =  " "
    #发送数据
    def send(self, data):
        #串口收发的数据是bytes类型，通过encode()将str转变为bytes
        self.port.write(data.encode("gbk"))
    #接收数据
    def receive(self):        
        while self.working:
            #休眠一个微小的时间，可以避免无谓的CPU占用
            time.sleep(0.001)
            if self.port.in_waiting > 0 :
                #串口收发的数据是bytes类型，通过decode()将bytes转变为str
                self.Rev_data = self.port.readline().decode("gbk")
               
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

    while True:
        time.sleep(1)
        s.send(s.Rev_data)
        print(s.Rev_data)
        

