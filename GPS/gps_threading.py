import os
import time
import serial
import threading

class Config:
    # 端口号
    serialPort = "/dev/ttyUSB0"
    # 波特率 
    baudRate = 38400

class GpsReader:
    def __init__(self):
        self.Longitude = 0  #经度
        self.Latitude = 0   #纬度
        self.UTC = 0        #UTC     
        self.port = serial.Serial(Config.serialPort, Config.baudRate,timeout = 1)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()
        self.working = False
    #打开
    def open(self):
        if not self.port.isOpen():
            self.port.open()
    #关闭
    def close(self):
        self.port.close()
    #发送数据
    def send(self,data):
        self.port.write(data)
    #接收数据
    def receive(self):        
        while self.working:
            #休眠一个微小的时间，可以避免无谓的CPU占用
            time.sleep(0.001)
            if self.port.in_waiting > 0 :
                GpsBytes = self.port.readline().decode("gbk")#startswith只能识别bytes
                
                #只匹配以“$GNRMC”开头的数据
                if GpsBytes.startswith('$GNRMC') != 0:
                    GpsArray = GpsBytes.split(',') #split通过指定分隔符对字符串进行切片
                    #print(GpsArray) #检查接收情况

                    if len(GpsArray) != 14:
                        print('数据不完整')
                        continue#检查数据完整度
                    if GpsArray[2] == 'V' :
                        print('当前卫星定位无效')
                    elif GpsArray[2] == 'A' :
                        print('定位正常')
                        #年月日 时分秒
                        UTC = '20' + GpsArray[9][4:6] + '/' + GpsArray[9][2:4] + '/'+ GpsArray[9][0:2]         
                        self.UTC = UTC + ' ' + GpsArray[1][0:2] + ':' + GpsArray[1][2:4] + ':' + GpsArray[1][4:6] 
                        #经纬度（单位：º） 
                        #round(a ,x ) 保留数字a小数点后x位        
                        self.Longitude = round(int(GpsArray[3][0:2])+float(GpsArray[3][2:11])/60 ,6)
                        self.Latitude = round(int(GpsArray[5][0:3])+float(GpsArray[5][3:12])/60 ,6)
                    else :
                        print('数据有误，等待刷新')    
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
    g=GpsReader()
    g.start()

    while True:
        time.sleep(1)
        print(g.UTC)
        print(g.Latitude)
        print(g.Longitude)
        
