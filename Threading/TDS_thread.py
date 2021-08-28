# -*- coding:utf-8 -*-
import os
import time
import threading
from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board

#添加溶解性固体总量（Total Dissolved Solids）测量类
class TdsReader:
    #初始化函数
    def __init__(self):
        self.iniVariable()
        self.board_detect() 
        while self.board.begin() != self.board.STA_OK:    # Board begin and check board status
            self.print_board_status()
            print("board begin faild")
            time.sleep(2)
        print("board begin success")
        self.board.set_adc_enable()
        self.working = False
    #初始化变量
    def iniVariable(self): 
        self.board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10  
        self.TdsVal  = 0
        
    def board_detect(self):
        l = self.board.detecte()
        print("Board list conform:")
        print(l)
        
    ''' print last operate status, users can use this variable to determine the result of a function call. '''
    def print_board_status(self):
      if self.board.last_operate_status == self.board.STA_OK:
        print("board status: everything ok")
      elif self.board.last_operate_status == self.board.STA_ERR:
        print("board status: unexpected error")
      elif self.board.last_operate_status == self.board.STA_ERR_DEVICE_NOT_DETECTED:
        print("board status: device not detected")
      elif self.board.last_operate_status == self.board.STA_ERR_PARAMETER:
        print("board status: parameter error")
      elif self.board.last_operate_status == self.board.STA_ERR_SOFT_VERSION:
        print("board status: unsupport board framware version")

    #数据测量和解析，目前仅测量adc的数据，数据再解析后面再做
    def decodeData(self):
        while self.working:
            self.TdsVal = self.board.get_adc_value(self.board.A0)   # A0 channels read
            #val = board.get_adc_value(board.A1)   # A1 channels read
            #val = board.get_adc_value(board.A2)   # A2 channels read
            #val = board.get_adc_value(board.A3)   # A3 channels read
            time.sleep(2)

    #开始工作
    def start(self):
        #开始数据读取线程
        t = threading.Thread(target=self.decodeData)
        #将当前线程设为子线程t的守护线程，这样一来，当前线程结束时会强制子线程结束
        t.setDaemon(True)
        self.working = True
        t.start()
    #停止工作
    def stop(self):
        self.working = False
        
#如果本文件被引用则面函数不被执行
if __name__=="__main__":
    t=TdsReader()#创建一个类的实例，并且调用init函数
    t.start()

    while True:
        time.sleep(1)
        print("channel: A0, value: %d" %t.TdsVal)
        print("")

