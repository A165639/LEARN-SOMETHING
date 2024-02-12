from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from pymysql import *
import pymysql
from time import strftime
from datetime import datetime
import cv2
from cv2 import *
import numpy as np
import os
class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x1500+0+0")
        self.root.title("face recognition system")

        self.root.configure(bg='gray')

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",25,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1380,height=50 )

#  back button ============       
        return_win=Button(self.root,command=self.return_login,text="Back",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="blue",bg="white",activeforeground="white",activebackground="red")
        return_win.place(x=3,y=8,width=80,height=35)

        def time():
                string=strftime("%H:%M:%S %p")
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",13,"bold"),background="blue",foreground="white")
        lbl.place(x=1250,y=0,width=100,height=45)
        time()

# top image
        img_top=Image.open(r"D:\attendence management software\PHOTO\photos.jpg")
        img_top=img_top.resize((1450,300),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1450,height=250)
# button  
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=310,width=300,height=50)
#bottom image
        img_bottom=Image.open(r"D:\attendence management software\PHOTO\train.jpg")
        img_bottom=img_bottom.resize((1450,300),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=365,width=1450,height=300)

    def train_classifier(self):
        data_dir=("data") 
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # grayscale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #============= Train the classifier===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data set completed")

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()        