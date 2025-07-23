from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from time import strftime
from datetime import datetime
from student2 import Student2
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from attendance import Attendance
from developer import Developer
from help import Help
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1355x790+0+0")

        
        img3=Image.open(r"L_images\bg_image2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
# background image
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=710)
# frame 
        frame=Frame(self.root,bg='black')
        frame.place(x=510,y=130,width=350,height=450)
# userlogo
        img1=Image.open(r"L_images\userlogo.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        img1_label=Label(image=self.photoimg1,bg="black",borderwidth=0)
        img1_label.place(x=630,y=140,width=100,height=100)

        get_str=Label(frame,text="Login Details",font=("times New roman",20,"bold"),fg='white',bg='black')
        get_str.place(x=80,y=115)

       # user name Label
        username_label=Label(frame,text="Username :",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_label.place(x=65,y=155)

        self.txtuser=ttk.Entry(frame,font=(" times new roman",15))
        self.txtuser.place(x=40,y=185,width=250)

         # password  Label
        pass_label=Label(frame,text="Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
        pass_label.place(x=65,y=230)

        self.txtpass=ttk.Entry(frame,font=(" times new roman",15))
        self.txtpass.place(x=40,y=260,width=250)

        # icon images 

        img2=Image.open(r"L_images\userlogo.png")
        img2=img1.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        img1_label=Label(image=self.photoimg2,bg="black",borderwidth=0)
        img1_label.place(x=550,y=285,width=25,height=25)

        img4=Image.open(r"L_images\pass.png")
        img4=img4.resize((25,25),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        img1_label=Label(image=self.photoimg4,bg="black",borderwidth=0)
        img1_label.place(x=550,y=360,width=25,height=25)

        # login button
        btn_login=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        btn_login.place(x=100,y=300,width=120,height=35)

        # new register button
        register_button=Button(frame,text="New User Register here",command=self.rigester_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="white",activeforeground="white",activebackground="black")
        register_button.place(x=30,y=350,width=150)

        # forgate button 
        register_button=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,bg="black",fg="white",activeforeground="white",activebackground="black")
        register_button.place(x=10,y=380,width=150)

    def rigester_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please fill all the fields")
        elif self.txtuser.get()=="pavan" and self.txtpass.get()=="pavan123":
            messagebox.showinfo("Success","Welcome Pavan")
        else:
            conn=mysql.connector.connect(host="localhost", username="root",password="admin@12345",database="face_recognizer")
            mycursor=conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get(),
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showinfo("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main >0:
                    self.new_window=Toplevel(self.root)
                    self.app=FaceRecognition(self.new_window)

                else:
                    if not open_main:
                        return
                
                conn.commit()
                conn.close()
# reset password 
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Please select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="" :
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", username="root",password="admin@12345",database="face_recognizer")
            mycursor=conn.cursor()
            query=("SELECT * FROM register WHERE email=%s and security_Q=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_securityA.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register SET password=%s WHERE email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                mycursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset successfully",parent=self.root2)
                self.root2.destroy()

# forgate password window 
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", username="root",password="admin@12345",database="face_recognizer")
            mycursor=conn.cursor()
            query=("SELECT * FROM register WHERE email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","User not found "," enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgate password ")
                self.root2.geometry("400x400+510+150")
                l=Label(self.root2,text="forgate password",font=("times new roman",12,"bold"),fg="black",bg="white")
                l.place(x=0,y=10)

                # security
                security_Q=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="black", bg="white")
                security_Q.place(x=50,y=80)
                
                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman", 15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("select", "Your Birth Place ", "Your First Pet Name", "Your First School Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman", 15,"bold"),fg="black", bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                # new password
                new_password=Label(self.root2,text="New Password",font=("times new roman", 15,"bold"),fg="black", bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpasswod=ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_newpasswod.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset" ,font=("times new roman",15,"bold"),fg="white",bg="red")
                btn.place(x=50,y=300)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register window ")
        self.root.geometry("1355x690+0+0")

    # variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        

 # background image 
        img3=Image.open(r"L_images\bg_image2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=710)



# left image 
        self.bg1=ImageTk.PhotoImage(file=r"D:\face recogniition system\L_images\bg_image2.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

# frame
        frame=Frame(self.root,bg="white") 
        frame.place(x=520,y=100,width=700,height=550)
   
    # label
        register_lable=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="red",bg="white")
        register_lable.place(x=20,y=20)

    # label and entry field
    # fname
        fname=Label(frame,text="First Name", font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

    # lname
        lname=Label(frame,text="Last Name", font=("times new roman",15,"bold"),bg="white")
        lname.place(x=380,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=380,y=130,width=250)

    # contact
        contact=Label(frame,text="Contact", font=("times new roman",15,"bold"),bg="white")
        contact.place(x=380,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=380,y=200,width=250)

    # email
        email=Label(frame,text="Email", font=("times new roman",15,"bold"),bg="white")
        email.place(x=50,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=50,y=200,width=250)

    # security
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black", bg="white")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ ,font=("times new roman", 15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select", "Your Birth Place ", "Your First Pet Name", "Your First School Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman", 15,"bold"),fg="black", bg="white")
        security_A.place(x=380,y=240)

        self.text_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15,"bold"))
        self.text_security.place(x=380,y=270,width=250)

    # password
        pswd=Label(frame,text="Password",font=("times new roman", 15,"bold"),fg="black", bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

    # confirm passsword
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman", 15,"bold"),fg="black", bg="white")
        confirm_pswd.place(x=380,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman", 15,"bold"))
        self.txt_pswd.place(x=380,y=340,width=250)

     # check button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree The terms and conditions",font=("times new roman", 12,"bold"),onvalue=1,offvalue=0 )
        checkbtn.place(x=50,y=380)

    #register  button
        img=Image.open(r"D:\face recogniition system\L_images\register.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman", 15,"bold"))
        b1.place(x=50,y=420,width=200)

    # login button

        img1=Image.open(r"D:\face recogniition system\L_images\login.jpg")
        img1=img1.resize((200,40),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman", 15,"bold"))
        b2.place(x=380,y=420,width=200)



        # register function
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password doed not match",parent=self.root)
        elif self.var_check.get()== 0:
            messagebox.showerror("Error","Please agree to the terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root",password="admin@12345",database="face_recognizer")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, try another email",parent=self.root)
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                    

                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("success","Register Successfully")


    def return_login(self):
        self.root.destroy()

class FaceRecognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Main_window")

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
        self.iExit = messagebox.askyesno("Face Recognition", "Confirm if you want to Exit",parent=self.root)
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


  
                
        
    
if __name__ == "__main__":
    main()
