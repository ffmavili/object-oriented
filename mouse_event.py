from tkinter import *
class Fare:
    def __init__(self):
        pencere=Tk()
        pencere.title("fare")

        canvas=Canvas(pencere,bg="white",width=200,height=100)
        canvas.pack()

        canvas.bind("<Button-1>",self.fareişlem)
        canvas.bind("<Key>",self.klavyeişlem)
        canvas.focus_set()
        pencere.mainloop()
    def fareişlem(self,event):
        print("tıklandı:",event.x,event.y)
        print("ekrandaki yeri:",event.x_root,event.y_root)
        print("hangi butona tıklandı:",event.num)
    def klavyeişlem(self,event):
        print("keysym?",event.keysym)
        print("char?",event.char)
        print("keycode?",event.keycode)
Fare()