from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from pymysql import *
import pymysql
from time import strftime
from datetime import datetime
import cv2
from cv2 import *
import numpy
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x1500+0+0")
        self.root.title("face recognition system")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_course=StringVar()
        self.var_teacher=StringVar()

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

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",25,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1380,height=50 )

#  back button ============       
        return_win=Button(bg_img,command=self.return_login,text="Back",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="blue",bg="white",activeforeground="white",activebackground="red")
        return_win.place(x=15,y=7,width=80,height=35)

        def time():
                string=strftime("%H:%M:%S %p")
                lbl.config(text=string)
                lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",13,"bold"),background="blue",foreground="white")
        lbl.place(x=1250,y=0,width=100,height=50)
        time()
          #main frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=50,width=1325,height=680)

          #left label frame        
        left_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold" ),bg="white",fg="black")
        left_frame.place(x=10,y=10,width=700,height=500)

        img_left=Image.open(r"D:\attendence management software\PHOTO\l.jpg")
        img_left=img_left.resize((500,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=690,height=60)
          #current course details
        current_course_frame=LabelFrame(left_frame,bd=4,relief=RIDGE,text="current course details",font=("times new roman",10,"bold" ),bg="white",fg="black")
        current_course_frame.place(x=0,y=61,width=680,height=100)
          #department
        dep_label=Label(current_course_frame,text="department",font=("times new roman",15,"bold" ),bg="white")
        dep_label.grid(row=0,column=0,padx=3,sticky=W)
          #combo box
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",15,"bold" ),state="readonly")
        dep_combo["value"]=("select department","B-Tech","M-Tech","Diploma","Phamecy")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

          #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",15,"bold" ),bg="white")
        course_label.grid(row=0,column=2,padx=3,sticky=W)
          #combo box
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",15,"bold" ),state="readonly")
        course_combo["value"]=("select course","CSE","IT","Civil","Macanical","ECE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5)


          #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",15,"bold" ),bg="white")
        year_label.grid(row=1,column=0,padx=3,sticky=W)
          #combo box
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",15,"bold" ),state="readonly")
        year_combo["value"]=("select year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

         #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",15,"bold" ),bg="white")
        semester_label.grid(row=1,column=2,padx=3,sticky=W)
          #combo box
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",15,"bold" ),state="readonly")
        semester_combo["value"]=("select semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)


                                  
          #class student information
        class_student_frame=LabelFrame(left_frame,bd=4,relief=RIDGE,text="class student information",font=("times new roman",10,"bold" ),bg="white",fg="black")
        class_student_frame.place(x=0,y=160,width=680,height=500)

         #student ID    
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",15,"bold" ),bg="white")
        studentID_label.grid(row=0,column=0,padx=3,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=3,sticky=W)

          #student name    
        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",15,"bold" ),bg="white")
        studentname_label.grid(row=0,column=2,padx=3,sticky=W)

        studentIname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentIname_entry.grid(row=0,column=3,padx=3,sticky=W) 

          #class details    
        class_details_label=Label(class_student_frame,text="Class Division",font=("times new roman",15,"bold" ),bg="white")
        class_details_label.grid(row=1,column=0,padx=3,sticky=W)

        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=14,font=("times new roman",15,"bold" ),state="readonly")
        class_div_combo["value"]=("Select Division","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=3,sticky=W)
          
          #roll no    
        roll_no_label=Label(class_student_frame,text="Roll No",font=("times new roman",15,"bold" ),bg="white")
        roll_no_label.grid(row=1,column=2,padx=3,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=3,sticky=W) 

          #gender    
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",15,"bold" ),bg="white")
        gender_label.grid(row=2,column=0,padx=3,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=14,font=("times new roman",15,"bold" ),state="readonly")
        gender_combo["value"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=3,sticky=W)
         
         #dob    
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",15,"bold" ),bg="white")
        dob_label.grid(row=2,column=2,padx=3,sticky=W)

        sdob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        sdob_entry.grid(row=2,column=3,padx=3,sticky=W)

         #email    
        email_label=Label(class_student_frame,text="Email",font=("times new roman",15,"bold" ),bg="white")
        email_label.grid(row=3,column=0,padx=3,sticky=W)

        semail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        semail_entry.grid(row=3,column=1,padx=3,sticky=W)

         #phone    
        phone_label=Label(class_student_frame,text="Phone No",font=("times new roman",15,"bold" ),bg="white")
        phone_label.grid(row=3,column=2,padx=3,sticky=W)

        sphone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        sphone_entry.grid(row=3,column=3,padx=3,sticky=W)

           #address    
        address_label=Label(class_student_frame,text="Address",font=("times new roman",15,"bold" ),bg="white")
        address_label.grid(row=4,column=0,padx=3,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=3,sticky=W)

          #teacher    
        teacher_name_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",15,"bold" ),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=3,sticky=W)

        steacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        steacher_name_entry.grid(row=4,column=3,padx=3,sticky=W) 

           #radio buttons
        self.var_radio1=StringVar()
        radio_button1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radio_button1.grid(row=6,column=0,sticky=W)
        
        
        radio_button2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_button2.grid(row=6,column=1,sticky=W)

          #button frame        

        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=180,width=670,height=50)

        save_button=Button(button_frame,command=self.add_data,text="Save",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0,padx=3,pady=6)

        update_button=Button(button_frame,command=self.update_data,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1,padx=3,pady=6)

        delete_button=Button(button_frame,command=self.delete_dsata,text="Delete",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2,padx=3,pady=6)

        Reset_button=Button(button_frame,command=self.reset_data,text="Reset",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_button.grid(row=0,column=3,padx=3,pady=6)

         # photo buttons
        photo_button_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        photo_button_frame.place(x=0,y=230,width=670,height=50)

        take_photo_button1=Button(photo_button_frame,command=self.generate_dataset,text="Take a Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_button1.grid(row=0,column=0,padx=3,pady=6)

        update_photo_button2=Button(photo_button_frame,text="No Photo Sample",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_button2.grid(row=0,column=1,padx=3,pady=6)

#Right label frame        
        right_frame=LabelFrame(main_frame,bd=4,relief=RIDGE,text="Student Details",font=("times new roman",15,"bold" ),bg="white",fg="black")
        right_frame.place(x=710,y=10,width=600,height=500)

        img_right=Image.open(r"D:\attendence management software\PHOTO\img.jpg")
        img_right=img_right.resize((500,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=580,height=60)

          #   search system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=10,y=60,width=570,height=60)  

        search_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold" ),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=3,pady=4,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",15,"bold" ),state="readonly",width=5)
        search_combo["value"]=("select ","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=2,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=3,pady=2,sticky=W)

        search_button=Button(search_frame,text="Search",command=lambda: self.search_data(search_combo.get(), search_entry.get()),width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=3,pady=2,sticky=W)

        showall_button=Button(search_frame,text="Show All",command=self.show_all_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_button.grid(row=0,column=4,padx=3,pady=2,sticky=W)

         #tabel frame        
        tabel_frame=Frame(right_frame,bd=4,relief=RIDGE)
        tabel_frame.place(x=10,y=120,width=570,height=350)

        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.student_tabel=ttk.Treeview(tabel_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)

        self.student_tabel.heading("dep",text="department")
        self.student_tabel.heading("course",text="course")
        self.student_tabel.heading("year",text="year")
        self.student_tabel.heading("sem",text="semester")
        self.student_tabel.heading("id",text="studentID")
        self.student_tabel.heading("name",text="Name")
        self.student_tabel.heading("div",text="Division")
        self.student_tabel.heading("roll",text="Roll")
        self.student_tabel.heading("gender",text="Gender")
        self.student_tabel.heading("dob",text="DOV")
        self.student_tabel.heading("email",text="Email")
        self.student_tabel.heading("phone",text="Phone")
        self.student_tabel.heading("address",text="Address")
        self.student_tabel.heading("teacher",text="Teacher")
        self.student_tabel.heading("photo",text="PhotoSampleStatus")
        self.student_tabel["show"]="headings"

        self.student_tabel.column("dep",width=70)
        self.student_tabel.column("course",width=70)
        self.student_tabel.column("year",width=70)
        self.student_tabel.column("sem",width=70)
        self.student_tabel.column("id",width=70)
        self.student_tabel.column("name",width=100)
        self.student_tabel.column("roll",width=70)
        self.student_tabel.column("gender",width=70)
        self.student_tabel.column("div",width=70)
        self.student_tabel.column("dob",width=70)
        self.student_tabel.column("email",width=70)
        self.student_tabel.column("phone",width=70)
        self.student_tabel.column("address",width=70)
        self.student_tabel.column("teacher",width=70)
        self.student_tabel.column("photo",width=80)

        self.student_tabel.pack(fill=BOTH,expand=1)
        self.student_tabel.bind("<ButtonRelease>",self.get_cursur)
        self.fetch_data()

 #add data ********* sql connection *************************

    def add_data(self):
        if self.var_dep.get()=="select departmenet" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","all field are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
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
                messagebox.showinfo("success","student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)
            #messagebox.showinfo("success","welcome abdulmannan")  

# ****************** fetch data *******************            
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student")
        data=my_cursur.fetchall()

        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("",END,values=i)
            conn.commit()
            conn.close()    


# ************** update data************

    def get_cursur(self,event=""):
        cursur_focus=self.student_tabel.focus()
        content=self.student_tabel.item(cursur_focus)
        data=content["values"]

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
       
        
#update function     *************************
    def update_data(self):
        if self.var_dep.get()=="select departmenet" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","all field are required",parent=self.root)  
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update datya",parent=self.root)
                if update>0:
                   conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
                   my_cursur=conn.cursor()
                   my_cursur.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where studentID=%s",(
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
                    if not update:
                       return    
                messagebox.showinfo("success","studetailnt details updated ",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)

#*****delete function***********
    def delete_dsata(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("erroe","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=pymysql.connect(host="localhost",user="root",passwd="1234@",database="facerecognition")
                    my_cursur=conn.cursor()
                    sql="delete from student where studentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursur.execute(sql,val)
                else:
                    if not delete:
                         return
                messagebox.showinfo("deleted","studetailnt details deleted ",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                                 
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
# ********* reset data *********
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
       # self.var_radio2.set("")
# search ****************************************************************************
    def search_data(self, criteria, term):
        # Perform the search based on the selected criteria
        query = ""

        if criteria == "Roll No":
            query = f"SELECT * FROM student WHERE studentID = '{term}'"
        elif criteria == "Phone No":
            query = f"SELECT * FROM student WHERE phone = '{term}'"

        # Execute the query
       # self.cursor.execute(query)
        search_result = self.cursor.fetchall()

        # Display the search result (replace this with how you want to display the result)
        print(search_result)

    def show_all_data(self):
        # Retrieve all data from the table
        query = "SELECT * FROM student"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()

        # Display all data (replace this with how you want to display the result)
        print(all_data)

    
# ***************** generate data set or take a photo sample***********


    def generate_dataset(self):
        if self.var_dep.get()=="select departmenet" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","all field are required",parent=self.root)  
        else:
             try:
                conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
                my_cursur=conn.cursor()
                my_cursur.execute("select * from student")
                myresult=my_cursur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursur.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where studentID=%s",(
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
                                                                                            self.var_std_id.get()==id+1                       
                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
#*******load pree defain data********
                face_classifier=cv2.CascadeClassifier('D:\\attendence management software\\haarcascade_frontalface_default.xml')

                def face_croped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
#scaling factor 1.3 or minimum neighbor 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(300,300))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0,),2)
                        cv2.imshow("croped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","generating data set completed!!")

             except Exception as es:
               messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)

    def return_login(self):
        self.root.destroy()     
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
        
