from tkinter import *
from tkinter import ttk
import os
from time import strftime
from datetime import datetime
import tkinter
from PIL import Image,ImageTk
from student import Student
#from new.update import Student
from train import train
from face_recognition import face_recognition
from attendence import attendence
from developer import developer
from chatbot import Chatbot

class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x1000+0+0")
        self.root.title("face recognition system")

        #first image
        img=Image.open(r"D:\attendence management software\PHOTO\collage.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        #second image
        img1=Image.open(r"D:\attendence management software\PHOTO\loby.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)

        #third image
        img2=Image.open(r"D:\attendence management software\PHOTO\iso.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        #bg image
        img3=Image.open(r"D:\attendence management software\PHOTO\bg.jpg")
        img3=img3.resize((1450,570),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1450,height=570)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1380,height=50 )
#  back button ============       
        return_win=Button(bg_img,command=self.return_login,text="LogOut",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="red")
        return_win.place(x=1290,y=7,width=60,height=35)
    
#===========time===========
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",13,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=100,height=50)
        time()    

        #student details button image
        
        img4=Image.open(r"D:\attendence management software\PHOTO\student.png")
        img4=img4.resize((200,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=180)

        b1_1=Button(bg_img,text="student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=270,width=200,height=40)

        #face dedector face button
        img5=Image.open(r"D:\attendence management software\PHOTO\face.jpg")
        img5=img5.resize((200,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=100,width=200,height=180)

        b2_2=Button(bg_img,text="face detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=400,y=270,width=200,height=40)

        #Attendence button
        img6=Image.open(r"D:\attendence management software\PHOTO\attendence.jpg")
        img6=img6.resize((200,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b3.place(x=700,y=100,width=200,height=180)

        b3_3=Button(bg_img,text="Attendence ",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=700,y=270,width=200,height=40)


        #Help Desk Button
        img7=Image.open(r"D:\attendence management software\PHOTO\chat.jpg")
        img7=img7.resize((200,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chat)
        b4.place(x=1000,y=100,width=200,height=180)

        b4_4=Button(bg_img,text="Chat Bot",cursor="hand2",command=self.chat,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1000,y=270,width=200,height=40)

        #Train face button
        img8=Image.open(r"D:\attendence management software\PHOTO\train.jpg")
        img8=img8.resize((200,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=100,y=330,width=200,height=180)

        b5_5=Button(bg_img,text="train data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=100,y=500,width=200,height=40)

        #photos face button
        img9=Image.open(r"D:\attendence management software\PHOTO\photos.jpg")
        img9=img9.resize((200,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=400,y=330,width=200,height=180)

        b6_6=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=400,y=500,width=200,height=40)


        #developer face butoon
        img10=Image.open(r"D:\attendence management software\PHOTO\DEVELOPER.jpg")
        img10=img10.resize((200,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer)
        b7.place(x=700,y=330,width=200,height=180)

        b7_7=Button(bg_img,text="developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=700,y=500,width=200,height=40)


        #Exit face button
        img11=Image.open(r"D:\attendence management software\PHOTO\EXIT.jpg")
        img11=img11.resize((200,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b7.place(x=1000,y=330,width=200,height=180)

        b7_7=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=1000,y=500,width=200,height=40)
    
    def open_img(self):
        os.startfile(r"D:\attendence management software\data")


    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return        

#========== connectinh other page command========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendence(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window) 

    def chat(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window)      
    
    def return_login(self):
        self.root.destroy()
if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
