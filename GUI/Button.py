# encoding:utf8

import Tkinter 

root = Tkinter.Tk()	
root.geometry('500x300') 
							#生成root主窗口
label = Tkinter.Label(root,text='Hello,GUI')	#生成标签
label.pack()
var = Tkinter.StringVar()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
									#将标签添加到主窗口
button1 = Tkinter.Button(root,text='Button1',command=hit_me) 	#生成button1
button1.pack()         		#将button1添加到root主窗口
root.mainloop()									#进入消息循环（必需组件）
