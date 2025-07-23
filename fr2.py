from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from datetime import datetime
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1355x690+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", 
                         font=("times new roman", 35, "bold"), 
                         bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1355, height=45)

        # Left image
        img_top = Image.open(r"images\facerecognition1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Right image
        img_bottom = Image.open(r"images\facerecognition2.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=600, y=55, width=950, height=700)

        # Recognition button
        b1_1 = Button(f_lbl2, text="Face Recognition", 
                     command=self.face_recog, cursor="hand2", 
                     font=("times new roman", 15, "bold"), 
                     bg="green", fg="white")
        b1_1.place(x=350, y=550, width=200, height=40)

    def mark_attendance(self, student_id, roll, name, department):
        """Mark attendance in CSV file if not already recorded"""
        filename = "attendance.csv"
        
        # Create file if it doesn't exist
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("StudentID,RollNo,Name,Department,Time,Date,Status\n")
        
        with open(filename, "r+") as f:
            my_datalist = f.readlines()
            attendance_list = [line.split(",")[0] for line in my_datalist if line.strip()]
            
            if student_id not in attendance_list:
                now = datetime.now()
                date_str = now.strftime("%d/%m/%Y")
                time_str = now.strftime("%H:%M:%S")
                f.write(f"{student_id},{roll},{name},{department},{time_str},{date_str},Present\n")

    def face_recog(self):
        """Main face recognition function"""
        def draw_boundary(img, classifier, recognizer, scaleFactor=1.1, minNeighbors=5):
            """Detect faces and draw boundaries with recognition info"""
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Predict the face
                id, confidence = recognizer.predict(gray_img[y:y+h, x:x+w])
                
                # Calculate confidence percentage (LBPH returns lower values for better matches)
                confidence_percent = round(100 - confidence)
                
                # Only proceed if confidence is above threshold (adjust as needed)
                if confidence_percent > 50:  # Lower this value if too strict
                    # Fetch data from database
                    conn = None
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="admin@12345",
                            database="face_recognizer"
                        )
                        cursor = conn.cursor()
                        
                        # Debug: Print the predicted ID
                        print(f"Predicted ID: {id}, Confidence: {confidence_percent}%")
                        
                        cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
                        result = cursor.fetchone()
                        
                        if result:
                            student_id, name, roll, department = result
                            
                            # Debug: Print fetched data
                            print(f"Fetched from DB: ID:{student_id}, Name:{name}, Roll:{roll}, Dept:{department}")
                            
                            # Display info on frame
                            cv2.putText(img, f"ID: {student_id}", (x, y-80), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Roll: {roll}", (x, y-55), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name: {name}", (x, y-30), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Dept: {department}", (x, y-5), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Confidence: {confidence_percent}%", (x, y+h+20), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                            
                            # Mark attendance
                            self.mark_attendance(student_id, roll, name, department)
                        else:
                            cv2.putText(img, "Unknown ID", (x, y-5), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                            print(f"No record found for ID: {id}")
                    
                    except mysql.connector.Error as err:
                        print(f"Database error: {err}")
                    finally:
                        if conn and conn.is_connected():
                            conn.close()
                else:
                    cv2.putText(img, "Unknown Face", (x, y-5), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    cv2.putText(img, f"Confidence: {confidence_percent}%", (x, y+h+20), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)

        # Load classifiers and recognizer
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        if face_cascade.empty():
            messagebox.showerror("Error", "Haar Cascade file not loaded!")
            return
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        if os.path.exists("classifier.xml"):
            recognizer.read("classifier.xml")
            print("Classifier loaded successfully")
        else:
            messagebox.showerror("Error", "Classifier file not found!")
            print("Classifier file not found at:", os.path.abspath("classifier.xml"))
            return

        # Start video capture
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open video capture!")
            return
        
        # Create window with proper size
        cv2.namedWindow("Face Recognition", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Face Recognition", 800, 600)
        
        while True:
            ret, frame = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to capture frame!")
                break
                
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Process frame
            draw_boundary(frame, face_cascade, recognizer)
            
            # Display frame
            cv2.imshow("Face Recognition", frame)
            
            # Exit on ESC key
            if cv2.waitKey(1) == 27:
                break
                
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()