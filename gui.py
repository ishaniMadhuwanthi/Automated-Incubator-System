# import tkinter as tk
# from tkinter import filedialog, Text
# import os
#
# root = tk.Tk()
#
# canvas = tk.Canvas(root, height=500, width=700, bg='blue')
# canvas.pack()
#
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
#
# root.mainloop()

from tkinter import *


window = Tk()
# add widgets here

window.title('Eggs Encubator-Scada System')
window.geometry("500x300")

lbl0=Label(window, text="Incubator System", fg='red', font=("Helvetica", 16))
lbl0.place(x=90, y=20)

col1=Label(window, text="Indicator", fg='Green', font=("Helvetica", 16))
col1.place(x=200, y=60)

col2=Label(window, text="Controller", fg='green', font=("Helvetica", 16))
col2.place(x=350, y=60)

lbl1=Label(window, text="Temperature", fg='Black', font=("Helvetica", 16))
lbl1.place(x=10, y=100)

lbl2=Label(window, text="Pressure", fg='Black', font=("Helvetica", 16))
lbl2.place(x=10, y=150)

lbl3=Label(window, text="Light Intensity", fg='Black', font=("Helvetica", 16))
lbl3.place(x=10, y=200)

endlbl=Label(window, text="Change", fg='Black', font=("Helvetica", 16))
endlbl.place(x=100, y=250)


window.mainloop()