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

gui = Tk(className='Python Examples')

# set window size
gui.geometry("400x200")
#set window color
gui['bg']='green'

# create button
button = Button(gui, text='Button', width=40, height=3,  bg='#ffffff', fg='#000000', activebackground='#0052cc', activeforeground='#aaffaa')
# add button to gui window
button.pack()

gui.mainloop()