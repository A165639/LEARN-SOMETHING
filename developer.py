from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from pymysql import *
import pymysql
import cv2
from time import strftime
from datetime import datetime
from cv2 import *
import numpy as np
import os
class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("face recognition system")

        self.root.configure(bg="darkblue")

        title_lbl=Label(self.root,text="Developer",font=("times new roman",25,"bold"),bg="lightblue",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1380,height=50 )

#  back button ============       
        return_win=Button(self.root,command=self.return_login,text="Back",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="blue",bg="white",activeforeground="white",activebackground="red")
        return_win.place(x=0,y=7,width=80,height=35)

        def time():
                string=strftime("%H:%M:%S %p")
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",13,"bold"),background="lightblue",foreground="darkblue")
        lbl.place(x=1250,y=0,width=100,height=45)
        time()

# top image
        img_top=Image.open(r"D:\attendence management software\PHOTO\train.jpg")
        img_top=img_top.resize((1450,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1450,height=700)

        #main frame
        main_frame=Frame(f_lbl,bd=2,bg="lightblue")
        main_frame.place(x=1000,y=0,width=500,height=650)
       

        #img_top1=Image.open(r"D:\attendence management software\PHOTO\abdul.jpg")
        #img_top=img_top1.resize((800,20),Image.LANCZOS)
        #self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        #f_main=Label(main_frame,image=self.photoimg_top1)
        #f_main.place(x=0,y=0,width=200,height=200)

#==devaloper=========
        dev_label=Label(main_frame,text="Name - Abdul Mannan",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Age - 25 Year",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="Gender - Male",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=75)

        dev_label=Label(main_frame,text="Education - B-Tech",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=110)

        dev_label=Label(main_frame,text="Course - science Engineering",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=145)

        dev_label=Label(main_frame,text="Project - Mejor Project-1",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=180)

        dev_label=Label(main_frame,text="Address - Hyderabad",font=("times new roman",15,"bold" ),fg="darkblue",bg="lightblue")
        dev_label.place(x=0,y=215)

        #img_top2=Image.open(r"D:\attendence management software\PHOTO\developer.jpg")
        #img_top=img_top2.resize((495,645),Image.LANCZOS)
        #self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        
        #f_d=Label(main_frame,image=self.photoimg_top2)
        #f_d.place(x=5,y=205,width=495,height=645)
   
    def return_login(self):
        self.root.destroy()
if __name__ == "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()                