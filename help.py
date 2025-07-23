from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1355x690+0+0")
        self.root.title("Help window")

        #title 
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1355,height=45)


    # bg image

        img_top=Image.open(r"images\help1.jpg")   
        img_top=img_top.resize((1355,690),Image.LANCZOS) 
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1355,height=690)

    #title 
        title_lbl=Label(f_lbl,text="mca2322032@smsvaranasi.in",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=350,y=200,width=650,height=45)

        title_lbl=Label(f_lbl,text="mca2322045@smsvaranasi.in",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=350,y=260,width=650,height=45)

        title_lbl=Label(f_lbl,text="mca2322046@smsvaranasi.in",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=350,y=320,width=650,height=45)

        title_lbl=Label(f_lbl,text="mca2322055@smsvaranasi.in",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=350,y=380,width=650,height=45)







if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()