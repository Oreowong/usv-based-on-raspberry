# -*- coding: utf-8 -*-                     #通过声明可以在程序中书写中文
import RPi.GPIO as GPIO                     #引入RPi.GPIO库函数命名为GPIO
import time                                 #引入计时time函数
# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)                    #将GPIO编程方式设置为BOARD模式
# 输出模式
GPIO.setup(12, GPIO.OUT)                    #将GPIO引脚11设置为输出引脚

p = GPIO.PWM(12, 50)
p.start(8)
input('点击回车停止：')   # 在 Python 2 中需要使用 raw_input
p.stop()
GPIO.cleanup()
