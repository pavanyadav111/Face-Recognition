from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student2 import Student2
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class FaceRecognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Main window")

    #first image 
        img=Image.open(r"images\face.webp")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=130)

    # second image
        img1=Image.open(r"images\face.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

    #third image
        img2=Image.open(r"images\face4.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

    # background image 
        img3=Image.open(r"images\face5.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


    #title 
        title_lbl=Label(bg_img,text="FACE RECOGNITION Attendance  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

  

    #student button 

        img4=Image.open(r"images\student.png")
        img4=img4.resize((220,200),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=150,y=80,width=220,height=200)


        b1_1=Button(bg_img,text="student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=150,y=280,width=220,height=40)

    # Detect face button
     
        img5=Image.open(r"images\face.jpg")
        img5=img5.resize((200,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=220,height=220)


        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=400,y=280,width=220,height=40)

    # Attendance face button
     
        img6=Image.open(r"images\attendance.png")
        img6=img6.resize((200,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=650,y=80,width=220,height=220)


        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=650,y=280,width=220,height=40)

    # Help desk button

        img7=Image.open(r"images\help.png")
        img7=img7.resize((200,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=900,y=80,width=220,height=220)


        b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=900,y=280,width=220,height=40)
        

        
    # image trainned

        img8=Image.open(r"images\trained.png")
        img8=img8.resize((200,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=330,width=220,height=200)


        b1_1=Button(bg_img,text="Image Trainned",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=150,y=500,width=220,height=40)

    # Photos button

        img9=Image.open(r"images\photos.png")
        img9=img9.resize((200,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=330,width=220,height=200)


        b1_1=Button(bg_img,text="Photo Gallery",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=400,y=500,width=220,height=40)

    # Developer Button

        img10=Image.open(r"images\developer.png")
        img10=img10.resize((200,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=650,y=330,width=220,height=200)


        b1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=650,y=500,width=220,height=40)

    # Exit Button
        img11=Image.open(r"images\exit.png")
        img11=img11.resize((200,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=900,y=330,width=220,height=200)


        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=900,y=500,width=220,height=40)


    def open_img(self):
        os.startfile("data")


# exit function

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Confirm if you want to Exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
    
        else:
            return



# button function 

   # student button function

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student2(self.new_window)

# train data function
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

# face data function
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


# attendance data function

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

# developer data function
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)



# help data function
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)





if __name__== "__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()