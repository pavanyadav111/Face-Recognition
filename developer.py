from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1355x690+0+0")
        self.root.title("Developer Window")

        # Title
        title_lbl = Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1355, height=45)

        # Background image
        img_top = Image.open(r"images\developer1.jpg")
        img_top = img_top.resize((1355, 690), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1355, height=690)

        # Developer information
        devs = [
            {"name": "Pavan Kumar Yadav", "desc": "I am Python and \n Machine Learning  Developer", "img": r"images\photo.jpeg"},
            {"name": "Rohit YAdav ", "desc": "I am Python Developer", "img": r"images\rohit.jpeg"},
            {"name": "Sonam Rai", "desc": "I am Python Developer", "img": r"images\sonam.jpeg"},
            {"name": "Sakshi Pathak", "desc": "I am Python Developer", "img": r"images\sakshi.jpeg"}
        ]

        #  developer frames
        for idx, dev in enumerate(devs):
            x_pos = 50 + idx * 300

            main_frame = Frame(f_lbl, bd=2, relief=RIDGE, bg="white")
            main_frame.place(x=x_pos, y=100, width=280, height=400)

            # Image
            img = Image.open(dev["img"])
            img = img.resize((200, 200), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)

            label_img = Label(main_frame, image=photoimg)
            label_img.image = photoimg  # Keep a reference
            label_img.place(x=40, y=10, width=200, height=200)

            # Name
            name_lbl = Label(main_frame, text=dev["name"], font=("times new roman", 15, "bold"), bg="white", fg="black")
            name_lbl.place(x=40, y=220)

            # Description
            desc_lbl = Label(main_frame, text=dev["desc"], font=("times new roman", 12, "bold"), bg="white", fg="black")
            desc_lbl.place(x=40, y=260)



if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()