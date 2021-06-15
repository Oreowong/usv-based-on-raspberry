#!/usr/bin/python3
#encoding:utf8

import threading
import time

from pwm_thread import Pwmthread
from jy901 import SensorReader
from jy901 import DataParser
from camera_thread import Camthread
from serial_thread import Serialthread 

def main():
        #开启无线数传线程
        ser = Serialthread()
        ser.start()
        #开启手动控制线程
        p = Pwmthread(ser)
        p.start()
        #开启姿态传感器数据读取线程
        s = SensorReader()
        s.start()
        #开启姿态解算线程
        j = DataParser(s)
        j.start()
        #开启摄像头视频实时传输线程
        c = Camthread()
        c.start()  
        while True:
                time.sleep(1)
                print("加速度",j.a)#加速度
                print("角速度:",j.w)#角速度
                print("角度:",j.Angle)#角度
                print("温度:",j.Temperature)#温度
                print("mag:",j.h)
                ser.send(p.Direct)
                print(p.Direct)

if __name__ == '__main__':
        main()
