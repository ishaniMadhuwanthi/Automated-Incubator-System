# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:20:58 2020
@author: lenovo
"""

from opcua import Server
from Arduino import Arduino
import datetime
import tkinter as tk
from tkinter import *
import random

server = Server()

url = "opc.tcp://127.0.0.1:3030"
server.set_endpoint(url)

name = "OPCUA SIMULATION SERVER"
addspace = server.register_namespace(name)
#------
win = tk.Tk()
win.title("Automated Incubating System")
win.geometry('600x300')


topic = Label(win, text="Automated Incubator System", fg='red', font=("Helvetica", 16))
topic.place(x=200, y=20)

#-----------------
board = Arduino("11200", port="COM7")
board.pinMode(13, "OUTPUT")
board.pinMode(12, "OUTPUT")
board.pinMode(11, "OUTPUT")
def start():
    board.digitalWrite(11, "HIGH")

def stop():
    board.digitalWrite(11, "LOW")
    board.digitalWrite(12, "HIGH")
#-----------

node = server.get_objects_node()

param = node.add_object(addspace, "Parameters")

Temp = param.add_variable(addspace, "Temperature", 0)
Light = param.add_variable(addspace, "Light Intensity", 0)
Press = param.add_variable(addspace, "Pressure", 0)
Time = param.add_variable(addspace, "Time", 0)
Temp.set_writable()
Press.set_writable()
Light.set_writable()
Time.set_writable()
server.start()
print("Server Started at {} ".format(url))

def readSensors():
    output_2.set(random.choice([5,6,7,8,9,10]))
    output_1.set(random.choice([28,29,30,31,32]))
    output_3.set(random.choice([6,7]))
    win.after(1000, readSensors)



#------
output_1 = tk.StringVar()
output_2 = tk.StringVar()
output_3 = tk.StringVar()

measuredValues = [0, 1, 2, 3, 4, 5]
value0 = str(measuredValues[0])
value1 = str(measuredValues[1])
value2 = str(measuredValues[2])

output_1.set(value0)
output_2.set(value1)
output_3.set(value2)
#------------------------

#temp
lbl1 = Label(win, text="Temperature", fg='Black', font=("Helvetica", 16))
lbl1.place(x=10, y=100)
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=180, y=110)

rbtn = Button(win, bg='red', width=2)
rbtn.place(x=300, y=110)
gbtn = Button(win, bg='green', width=2)
gbtn.place(x=330, y=110)
ybtn = Button(win, bg='yellow', width=2)
ybtn.place(x=360, y=110)

btn = Button(win, text='ON', bg='purple', fg='white', width=5, command = start)
btn.place(x=450, y=110)
btn = Button(win, text='OFF', bg='purple', fg='white', width=5,command = stop)
btn.place(x=500, y=110)
#pressure
lbl2=Label(win, text="Pressure", fg='Black', font=("Helvetica", 16))
lbl2.place(x=10, y=150)
output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=180, y=160)

rbtn = Button(win, bg='red', width=2)
rbtn.place(x=300, y=160)
gbtn = Button(win, bg='green', width=2)
gbtn.place(x=330, y=160)
ybtn = Button(win, bg='yellow', width=2)
ybtn.place(x=360, y=160)



#light
lbl3=Label(win, text="Light Intensity", fg='Black', font=("Helvetica", 16))
lbl3.place(x=10, y=200)
output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=180, y=210)

rbtn = Button(win, bg='red', width=2)
rbtn.place(x=300, y=210)
gbtn = Button(win, bg='green', width=2)
gbtn.place(x=330, y=210)
ybtn = Button(win, bg='yellow', width=2)
ybtn.place(x=360, y=210)

#----------------
TIME = datetime.datetime.now()
T = output_1
PH = output_2
IR = output_3
print(T, PH, IR, TIME)

Temp.set_value(T)
Press.set_value(PH)
Light.set_value(IR)
Time.set_value(TIME)


win.after(1000, readSensors)
win.mainloop()
