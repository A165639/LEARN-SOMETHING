from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import cv2
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
import pymysql
from student import Student
import sqlite3
import numpy as np
import csv
from time import strftime
from datetime import datetime

class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x1000+0+0")
        self.root.title("face_recognition")

        self.root.configure(bg='gray')

#==========LEFT IMAGE========
        face_recognition_lbl=Label(self.root,text="Face Recognition",font=("times new roman",25,"bold"),bg="blue",fg="white")
        face_recognition_lbl.place(x=0,y=0,width=1380,height=50 )

 #  back button ============       
        return_win=Button(self.root,command=self.return_login,text="Back",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="blue",bg="white",activeforeground="white",activebackground="red")
        return_win.place(x=5,y=7,width=80,height=35)
   # ===time ========     
        def time():
                string=strftime("%H:%M:%S %p")
                lbl.config(text=string)
                lbl.after(1000,time)


        lbl=Label(face_recognition_lbl,font=("times new roman",13,"bold"),background="blue",foreground="white")
        lbl.place(x=1250,y=0,width=100,height=45)
        time()
         
        img_left=Image.open(r"D:\attendence management software\PHOTO\photos.jpg")
        img_left=img_left.resize((700,700),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=700,height=700)

# =======RIGHT IMAGE==========
        img_right=Image.open(r"D:\attendence management software\PHOTO\faces.jpg")
        img_right=img_right.resize((650,700),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=700,y=55,width=650,height=700)

#=========button===============
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=210,y=560,width=220,height=50)
#=====attendence========

    def mark_attendence(self,i,r,n,d):
        with open(r"E:\python program file\New folder\build\exe.win-amd64-3.11\attendance_report\abdul.csv","r+",newline="\n") as f:
            my_data=f.readlines()
            name_list=[]
            for line in my_data:
                entry=line.split((","))
                name_list.append(entry[0])
                
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")
              

    #=========face recognition=====
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                try:
                    conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select Name from student where studentID="+str(id))
                    n=my_cursor.fetchone()
                    n = "+".join(n)
                
                    my_cursor.execute("select roll from student where studentID="+str(id))
                    r=my_cursor.fetchone()
                    r = "+".join(r)
                
                    my_cursor.execute("select dep from student where studentID="+str(id))
                    d=my_cursor.fetchone()
                    d = "+".join(d)
                
                    my_cursor.execute("select studentID from student where studentID="+str(id))
                    i=my_cursor.fetchone() 
                    i = "+".join(i)
      
                except Exception as es:
                    messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)
                    
                    if confidence > 77:
                        cv2.putText(img, f"Name:{n}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Dep:{d}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"ID:{i}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        self.mark_attendence(n, r, d, i)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]
                conn.commit()
                conn.close()
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("D:\\attendence management software\\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("D:\\attendence management software\\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()

    def return_login(self):
        self.root.destroy()       
                

if __name__ == "__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()         
