from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student2:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1355x690+0+0")
        self.root.title("Student register window ")

        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        # first image 
        img = Image.open(r"images\student1.png")
        img = img.resize((534,110), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=534, height=110)

        # second image
        img1 = Image.open(r"images\student2.png")
        img1 = img1.resize((534,110), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=405, y=0, width=534, height=110)

        # third image
        img2 = Image.open(r"images\student3.png")
        img2 = img2.resize((534,110), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=810, y=0, width=534, height=110)

        # background image 
        img3 = Image.open(r"images\face5.jpg")
        img3 = img3.resize((1350,610), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1330, height=610)

        # title 
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1330, height=30)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=30, width=1355, height=600)

        # left label frame 
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=0, width=640, height=525)

        img_left = Image.open(r"images\studentattend.png")
        img_left = img_left.resize((620,110), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=600, height=110)

        # current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=90, width=605, height=110)

        # department
        dep_label = Label(current_course_frame, text="Department :", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=15)
        dep_combo["values"] = ("Select Department", "Computer Science", "IT", "Electronics", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(current_course_frame, text="Course :", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", "12", "bold"), state="readonly", width=15)
        course_combo["values"] = ("Select Course", "MCA", "B.Tech", "M.Tech", "B.E", "M.E")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year :", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), width="20", state="readonly")
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester :", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), width="15", state="readonly")
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester","5th Semester", "6th Semester","7th Semester","8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class student Information", font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=200, width=615, height=300)

        # student ID
        studentId_label = Label(class_student_frame, text="Student ID: ", font=("times new roman", 13, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=15, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        studentName_label = Label(class_student_frame, text="Student Name :", font=("times new roman", 13, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=15, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # class division 
        class_division_label = Label(class_student_frame, text="Class Division :", font=("times new roman", 13, "bold"), bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), width="15", state="readonly")
        div_combo["values"] = ("A", "B", "C","D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll no 
        roll_no_label = Label(class_student_frame, text="Roll No :", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=15, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width="15", state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB 
        dob_label = Label(class_student_frame, text="Date of Birth", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=15, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=15, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phone no
        phone_no_label = Label(class_student_frame, text="Phone No", font=("times new roman", 13, "bold"), bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=15, font=("times new roman", 13, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=15, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_name_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 13, "bold"))
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=15, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # Radio buttons
        radiobutton1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="Yes")
        radiobutton1.grid(row=5, column=0)
       
        radiobutton2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
        radiobutton2.grid(row=5, column=1)

        # button frame
        btn_frame = Frame(class_student_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=610, height=80)

        # save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=15, font=("times new roman", 13, "bold"), bg="red", fg="white")
        save_btn.grid(row=0, column=0)

        # update button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=15, font=("times new roman", 13, "bold"), bg="red", fg="white")
        update_btn.grid(row=0, column=1)

        # delete button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=15, font=("times new roman", 13, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 13, "bold"), bg="red", fg="white")
        reset_btn.grid(row=0, column=3)

        # sample button frame 
        btn_frame1 = Frame(class_student_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=610, height=35)

        # sample photo button
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=30, font=("times new roman", 13, "bold"), bg="red", fg="white")
        take_photo_btn.grid(row=0, column=1)
    
    #update sample photo button
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", command=self.generate_dataset, width=30, font=("times new roman", 13, "bold"), bg="red", fg="white")
        update_photo_btn.grid(row=0, column=2)

        # Right label frame    
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Right_frame.place(x=660, y=0, width=660, height=520)

        # first image 
        img_right = Image.open(r"images\student1.png")
        img_right = img_right.resize((420,130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=650, height=130)

        # search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 13, "bold"))
        search_frame.place(x=5, y=135, width=650, height=70)

        # search label
        search_label = Label(search_frame, text="Search By: ", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), width="12", state="readonly")
        self.search_combo["values"] = ("Select", "Roll no.", "Phone no", "Student ID")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.search_entry = ttk.Entry(search_frame, width=14, font=("times new roman", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # search button
        search_btn = Button(search_frame, text="Search", command=self.search_data, width=12, font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_btn.grid(row=0, column=3)

        # show all button
        showAll_btn = Button(search_frame, text="Show All", command=self.fetch_data, width=12, font=("times new roman", 12, "bold"), bg="red", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=650, height=285)

        # scroll bar 
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")  
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSample")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ===================Function Declarations=====================

    # add data function

    def add_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" 
            or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="admin@12345", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===================Fetch data=====================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="admin@12345", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===================Get Cursor=====================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ===================Update Function=====================
    def update_data(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" 
            or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="admin@12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===================Delete Function=====================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="admin@12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===================Reset Function=====================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ===================Search Data=====================
    def search_data(self):
        if self.search_combo.get() == "Select" or self.search_entry.get() == "":
            messagebox.showerror("Error", "Please select option and enter information", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="admin@12345", database="face_recognizer")
                my_cursor = conn.cursor()
                
                if self.search_combo.get() == "Roll no.":
                    my_cursor.execute("select * from student where Roll=%s", (self.search_entry.get(),))
                elif self.search_combo.get() == "Phone no":
                    my_cursor.execute("select * from student where Phone=%s", (self.search_entry.get(),))
                elif self.search_combo.get() == "Student ID":
                    my_cursor.execute("select * from student where Student_id=%s", (self.search_entry.get(),))
                    
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===================Take Photo Sample and generate data samples =====================
    def take_sample(self):
        if (self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" 
            or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="admin@12345", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
    # load predifine data on face frontal from open cv 

                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        

                messagebox.showinfo("Result", "Data set generation completed successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


# generate data set 
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() =="" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="admin@12345",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult= my_cursor.fetchall()
                id = 0
                for x in myresult:  
                    id += 1
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                 # load predifine data on face frontal from open cv 
    
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3 scalling factor
                    #5 minmum neighbor
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
               
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","generating data set completed succefully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}.parent=self.root",parent=self.root)
        

            


   
if __name__ == "__main__":
    root = Tk()
    obj = Student2(root)
    root.mainloop()