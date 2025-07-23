from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1355x690+0+0")
        self.root.title("Attendance system window")

    # variables 
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        

         #first image 
        img=Image.open(r"images\attendancel1.jpg")
        img=img.resize((675,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=675,height=200)

    # second image
        img1=Image.open(r"images\attendancel2.jpg")
        img1=img1.resize((675,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=676,y=0,width=675,height=200)

    # background image 
        img3=Image.open(r"images\attendancel3.jpg")
        img3=img3.resize((1355,610),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1355,height=610)


    #title 
        title_lbl=Label(bg_img,text=" ATTENDANCE  MANAGEMENT   SYSTEM ",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1355,height=30)

        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1350,height=600)
    # left_ labael frame 

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=715,height=420)

        img_left=Image.open(r"images\studentattend.png")
        img_left=img_left.resize((700,100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=700,height=100)

    # frame inside left frame
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white" )
        left_inside_frame.place(x=0,y=105,width=710,height=250)

    # labels and entry

     # Attendance  ID

        AttendanceId_label=Label(left_inside_frame,text="Attendance Id: ",font=("times new roman",12,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",11,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    # Student roll no

        studentName_label=Label(left_inside_frame,text="Roll no. :",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("comicsansns",11,"bold"))
        studentID_entry.grid(row=0,column=3,padx=4,pady=8,sticky=W)

    # NAme of student
        nameLabel=Label(left_inside_frame,text="Name",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0,pady=8)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=22,font="comixsansns 11 bold")
        atten_name.grid(row=1,column=1,padx=4,pady=8)

    # department 
        dep_label=Label(left_inside_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=22,font="comsicsansns 11 bold")
        atten_dep.grid(row=1,column=3,padx=10,pady=8)

    # time of attendance
        timeLabel=Label(left_inside_frame,text="Time",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

    # date of attendance
        dateLabel=Label(left_inside_frame,text="Date",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=3,pady=8)

    # attendance status
        attendanceLabel=Label(left_inside_frame,text="Attendance status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=22,font="comicsansns 11 bold",state="readonly")
        self.atten_status['values']=('Present','Absent')
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

    # button frame
    
        btn_frame=Frame(left_inside_frame,bg="white",bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=210,width=710,height=70)

    # import csv button
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)

    # export csv button
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)

    # update button
        delete_btn=Button(btn_frame,text="Update",command=self.update_data ,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

    # reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="reset",width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)    


    # Right lavel frame    
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))
        Right_frame.place(x=725,y=10,width=615,height=420)

    # frame inside right label frame
        table_frame=Frame(Right_frame,bg="white",bd=2, relief=RIDGE)
        table_frame.place(x=0,y=5,width=610,height=360)

    # scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
       

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # fetch data function
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # import data csv function
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln,mode="r",newline='') as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            #self.showdatainattendancetable()

    

    # export  csv  data
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            
                
            with open(fln,mode="w",newline='',encoding='utf-8') as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("Data export","your data exported to"+os.path.basename(fln)+"Successfully")
                
        except Exception as es:
                  messagebox.showerror("Error",f" due to :{str(es)}",parent=self.root)

   
    # show data in attendance table function

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content= self.AttendanceReportTable.item(cursor_row)
        rows =content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

# update function
    def update_data(self):
    # ... [previous code until the CSV writing part] ...
    
    # Always ask for a new file to save to
        fln = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Save Updated CSV",
        filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
        parent=self.root,
        defaultextension=".csv"
        )
        if fln:
            with open(fln, mode='w', newline='', encoding='utf-8') as file:
             writer = csv.writer(file)
            writer.writerows(mydata)
        messagebox.showinfo("Success", f"Updated data saved to {os.path.basename(fln)}", parent=self.root)


# reset function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



    
                    
        
                           

if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()