import os
import threading
import time 

class Camthread:
	def __init__(self):
		self.working = False
	#使用mjpg-streamer来实时传输视频
	def receive(self):
		if self.working == True:
			os.system('/home/pi/mjpg-streamer-master/mjpg-streamer-experimental/mjpg_streamer -i "/home/pi/mjpg-streamer-master/mjpg-streamer-experimental/input_raspicam.so" -o "/home/pi/mjpg-streamer-master/mjpg-streamer-experimental/output_http.so -w /home/pi/mjpg-streamer-master/mjpg-streamer-experimental/www"')
    #开始工作
	def start(self):
		#开始数据读取线程
		t = threading.Thread(target=self.receive)
		#将当前线程设为子线程t的守护线程，这样一来，当前线程结束时会强制子线程结束
		t.setDaemon(True)
		self.working = True
		t.start()     	

if __name__=="__main__":
    c = Camthread()
    c.start()

    while True:
        time.sleep(1)
        
