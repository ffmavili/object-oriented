from tkinter import *
class Kaydırma:
    def __init__(self):
        pencere=Tk()

        frame1=Frame(pencere)
        frame1.pack()
        scrollbar=Scrollbar(frame1)
        scrollbar.pack(side="right",fill=Y)
        text=Text(frame1,width=40,height=10,wrap=WORD,yscrollcommand=scrollbar.set)
        text.pack()
        scrollbar.config(command=text.yview)
        pencere.mainloop()
Kaydırma()