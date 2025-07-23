from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman", 15,"bold"))
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

    



if __name__== "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()