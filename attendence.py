from tkinter import *
from tkinter import ttk,messagebox,filedialog
from PIL import Image,ImageTk
from pymysql import *
from time import strftime
from datetime import datetime
import pymysql
import cv2
import csv
import os
from cv2 import *
import numpy

mydata=[]
class attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1500+0+0")
        self.root.title("face recognition system")

        self.root.configure(bg="gray")

#===================variables=============

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()  
        self.var_atten_name=StringVar()  
        self.var_atten_dep=StringVar()  
        self.var_atten_time=StringVar()  
        self.var_atten_date=StringVar()  
        self.var_atten_attendence=StringVar()          

#==========LEFT IMAGE========
        img_left=Image.open(r"D:\attendence management software\PHOTO\photos.jpg")
        img_left=img_left.resize((700,700),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=700,height=150)

# =======RIGHT IMAGE==========
        img_right=Image.open(r"D:\attendence management software\PHOTO\faces.jpg")
        img_right=img_right.resize((700,700),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=700,y=0,width=700,height=150)

#==========bg image==========
        img3=Image.open(r"D:\attendence management software\PHOTO\bg.jpg")
        img3=img3.resize((1450,570),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        title_lbl=Label(self.root,text="Attendence Management System",font=("times new roman",25,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=155,width=1380,height=50 )

#  back button ============       
        return_win=Button(self.root,command=self.return_login,text="Back",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="blue",bg="white",activeforeground="white",activebackground="red")
        return_win.place(x=10,y=163,width=80,height=35)

        def time():
                string=strftime("%H:%M:%S %p")
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",13,"bold"),background="blue",foreground="white")
        lbl.place(x=1250,y=0,width=100,height=45)
        time()
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=210,width=1400,height=570)

# main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=5,width=1342,height=680)

#=======left side frame========
        left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Student Attendence Details",font=("times new roman",15,"bold" ),bg="white",fg="red")
        left_frame.place(x=2,y=2,width=690,height=500)

        img_Lframe=Image.open(r"D:\attendence management software\PHOTO\img.jpg")
        img_Lframe=img_left.resize((500,130),Image.LANCZOS)
        self.photoimg_Lframe=ImageTk.PhotoImage(img_Lframe)

        left_lbl=Label(left_frame,image=self.photoimg_Lframe)
        left_lbl.place(x=5,y=5,width=675,height=80)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=95,width=675,height=350)

# =======label entry=======
#=======attendence id=====
        attendenceId_label=Label(left_inside_frame,text="Attendence ID",font=("times new roman",15,"bold" ),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=3,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=3,sticky=W)

#=======roll
        rollLabel_label=Label(left_inside_frame,text="Roll",font=("times new roman",15,"bold" ),bg="white")
        rollLabel_label.grid(row=0,column=2,padx=3,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=3,sticky=W)

#=======Name
        nameLabel_label=Label(left_inside_frame,text="Name",font=("times new roman",15,"bold" ),bg="white")
        nameLabel_label.grid(row=1,column=0,padx=3,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=3,sticky=W)

#=======Department
        depLabel_label=Label(left_inside_frame,text="Department",font=("times new roman",15,"bold" ),bg="white")
        depLabel_label.grid(row=1,column=2,padx=3,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=3,sticky=W)

#=======Tme
        timeLabel_label=Label(left_inside_frame,text="Time:",font=("times new roman",15,"bold" ),bg="white")
        timeLabel_label.grid(row=2,column=0,padx=3,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=3,sticky=W)

#=======date
        timeLabel_label=Label(left_inside_frame,text="Date:",font=("times new roman",15,"bold" ),bg="white")
        timeLabel_label.grid(row=2,column=2,padx=3,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=3,padx=3,sticky=W)                               

#=====Attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence Status",bg="white",font="comicsansns 11 bold")
        attendenceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendence,width=18,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Persent","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

#========button frame        
        button_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=295,width=670,height=50)

        save_button=Button(button_frame,text="Import CSV",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0,padx=3,pady=6)

        update_button=Button(button_frame,text="Export CSV",command=self.exportCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1,padx=3,pady=6)

        delete_button=Button(button_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2,padx=3,pady=6)

        Reset_button=Button(button_frame,command=self.reset,text="Reset",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_button.grid(row=0,column=3,padx=3,pady=6)
        
#Right label frame        
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Atendence Details",font=("times new roman",15,"bold" ),bg="white",fg="red")
        right_frame.place(x=695,y=2,width=640,height=500)

        img_Rframe=Image.open(r"D:\attendence management software\PHOTO\img.jpg")
        img_Rframe=img_right.resize((500,130),Image.LANCZOS)
        self.photoimg_Rframe=ImageTk.PhotoImage(img_Rframe)

        right_lbl=Label(right_frame,image=self.photoimg_Rframe)
        right_lbl.place(x=5,y=5,width=625,height=80)

        tabel_frame=Frame(right_frame,bd=2,relief=RIDGE)
        tabel_frame.place(x=2,y=95,width=630,height=350)

#=======scroll bar==========
        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.AttendenceReportTabel=ttk.Treeview(tabel_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTabel.xview)
        scroll_y.config(command=self.AttendenceReportTabel.yview)


        self.AttendenceReportTabel.heading("id",text="Attendence ID")
        self.AttendenceReportTabel.heading("roll",text="Roll")
        self.AttendenceReportTabel.heading("name",text="Name")
        self.AttendenceReportTabel.heading("department",text="Department")
        self.AttendenceReportTabel.heading("time",text="Time")
        self.AttendenceReportTabel.heading("date",text="Date")
        self.AttendenceReportTabel.heading("attendence",text="Attendence")

        self.AttendenceReportTabel["show"]="headings"

        self.AttendenceReportTabel.column("id",width=100)
        self.AttendenceReportTabel.column("roll",width=100)
        self.AttendenceReportTabel.column("name",width=100)
        self.AttendenceReportTabel.column("department",width=100)
        self.AttendenceReportTabel.column("time",width=100)
        self.AttendenceReportTabel.column("date",width=100)
        self.AttendenceReportTabel.column("attendence",width=100)

        self.AttendenceReportTabel.pack(fill=BOTH,expand=0)

        self.AttendenceReportTabel.bind("<ButtonRelease>",self.get_cursur)

#================frtch data==============
    def fetchdata(self,rows):
        self.AttendenceReportTabel.delete(*self.AttendenceReportTabel.get_children())
        for i in rows:
            self.AttendenceReportTabel.insert("",END,values=i)
# import csv=====
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)    

# export csv=====
    def exportCsv(self):
        try:
           if len(mydata)<1:
              messagebox.showerror("No data","Nodata found",parent=self.root)
              return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
           with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                  exp_write.writerow(i)
                messagebox.showinfo("exported","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)        
#===========get data from csv file to entry field
    def get_cursur(self,event=""):
        cursur_row=self.AttendenceReportTabel.focus()
        content=self.AttendenceReportTabel.item(cursur_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

#=========reset data========
    def reset(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("Status")


    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=attendence(root)
    root.mainloop()        