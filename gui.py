import tkinter as tk
from tkinter import *
import random


def readSensors():
    output_1.set(random.choice([0, 1, 2, 3, 4, 5]))
    output_2.set(random.choice([0, 1, 2, 3, 4, 5]))
    output_3.set(random.choice([0, 1, 2, 3, 4, 5]))
    win.after(2000, readSensors)

win = tk.Tk()

win.title("Automated Incubating System")
win.geometry('600x300')
#win.configure(background='#CD5C5C')

topic = Label(win, text="Automated Incubator System", fg='red', font=("Helvetica", 16))
topic.place(x=200, y=20)

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

#indictor column
col1=Label(win, text="Indicator", fg='Green', font=("Helvetica", 16))
col1.place(x=300, y=60)

#controller column
col2=Label(win, text="Controller", fg='green', font=("Helvetica", 16))
col2.place(x=450, y=60)

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

btn = Button(win, text='ON', bg='purple', fg='white', width=5)
btn.place(x=450, y=110)
btn = Button(win, text='OFF', bg='purple', fg='white', width=5)
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

btn = Button(win, text='ON', bg='purple', fg='white', width=5)
btn.place(x=450, y=160)
btn = Button(win, text='OFF', bg='purple', fg='white', width=5)
btn.place(x=500, y=160)

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

btn = Button(win, text='ON', bg='purple', fg='white', width=5)
btn.place(x=450, y=210)
btn = Button(win, text='OFF', bg='purple', fg='white', width=5)
btn.place(x=500, y=210)


#change button
endlbl=Label(win, text="Change",fg='Black', font=("Helvetica", 16))
endlbl.place(x=100, y=250)

btn = Button(win, text = 'Clear !', bg='blue', fg='white', command = win.destroy, width=10)
btn.place(x=250, y=250)

win.after(1000, readSensors)
win.mainloop()
