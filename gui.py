from tkinter import *

class Gui:
    def __init__(self):
        window = Tk()

        # add widgets here

        window.title("Eggs Encubator-Scada System")
        window.geometry("600x300")
        # window.configure(bg='#856ff8')

        lbl0=Label(window, text="Incubator System", fg='red', font=("Helvetica", 16))
        lbl0.place(x=200, y=20)

        #indictor column
        col1=Label(window, text="Indicator", fg='Green', font=("Helvetica", 16))
        col1.place(x=300, y=60)

        #controller column
        col2=Label(window, text="Controller", fg='green', font=("Helvetica", 16))
        col2.place(x=450, y=60)

        #temperature
        lbl1=Label(window, text="Temperature", fg='Black', font=("Helvetica", 16))
        lbl1.place(x=10, y=100)
        entryTemp = Entry(window,width=15)
        entryTemp.place(x=180, y=110)

        rbtn = Button(window, bg='red', width=2)
        rbtn.place(x=300, y=110)
        gbtn = Button(window, bg='green', width=2)
        gbtn.place(x=330, y=110)
        ybtn = Button(window, bg='yellow', width=2)
        ybtn.place(x=360, y=110)

        btn = Button(window, text='ON', bg='purple', fg='white', width=5)
        btn.place(x=450, y=110)
        btn = Button(window, text='OFF', bg='purple', fg='white', width=5)
        btn.place(x=500, y=110)

        #pressure
        lbl2=Label(window, text="Pressure", fg='Black', font=("Helvetica", 16))
        lbl2.place(x=10, y=150)
        entryPre = Entry(window, width=15)
        entryPre.place(x=180, y=160)

        rbtn = Button(window, bg='red', width=2)
        rbtn.place(x=300, y=160)
        gbtn = Button(window, bg='green', width=2)
        gbtn.place(x=330, y=160)
        ybtn = Button(window, bg='yellow', width=2)
        ybtn.place(x=360, y=160)

        btn = Button(window, text='ON', bg='purple', fg='white', width=5)
        btn.place(x=450, y=160)
        btn = Button(window, text='OFF', bg='purple', fg='white', width=5)
        btn.place(x=500, y=160)

        #light intensity
        lbl3=Label(window, text="Light Intensity", fg='Black', font=("Helvetica", 16))
        lbl3.place(x=10, y=200)
        entryLight = Entry(window, width=15)
        entryLight.place(x=180, y=210)

        rbtn = Button(window, bg='red', width=2)
        rbtn.place(x=300, y=210)
        gbtn = Button(window, bg='green', width=2)
        gbtn.place(x=330, y=210)
        ybtn = Button(window, bg='yellow', width=2)
        ybtn.place(x=360, y=210)

        btn = Button(window, text='ON', bg='purple', fg='white', width=5)
        btn.place(x=450, y=210)
        btn = Button(window, text='OFF', bg='purple', fg='white', width=5)
        btn.place(x=500, y=210)

        #change button
        endlbl=Label(window, text="Change",fg='Black', font=("Helvetica", 16))
        endlbl.place(x=100, y=250)

        btn = Button(window, text = 'Change !', bg='blue', fg='white', command = window.destroy, width=10)
        btn.place(x=250, y=250)

        window.mainloop()




Gui()