from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class registers:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1550x800+0+0")
        self.root.title=("Login")
        # variables=
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_fname=StringVar()
        self.var_contect=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cnpss=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\attendence management software\PHOTO\loginimage.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=170,y=60,width=1000,height=500)

        left_frame=LabelFrame(frame,bd=4,relief=RIDGE,bg="white",fg="red")
        left_frame.place(x=2,y=2,width=500,height=595)
        
        img_left=Image.open(r"D:\attendence management software\PHOTO\register.jpg")
        img_left=img_left.resize((700,700),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=500,height=595)
#========right frame
        right_frame=LabelFrame(frame,bd=4,relief=RIDGE,bg="white",fg="red")
        right_frame.place(x=510,y=2,width=550,height=595)
        
        title_lbl=Label(right_frame,text="Ragister Here",font=("times new roman",20,"bold"),bg="white",fg="red")
        title_lbl.place(x=2,y=0,width=210,height=40 )

        left_inside_frame=LabelFrame(right_frame,background="gray",bd=4,relief=RIDGE,text="New user details",font=("times new roman",15,"bold" ),bg="white",fg="red")
        left_inside_frame.place(x=2,y=40,width=550,height=548)


        #student ID    
        studentID_label=Label(left_inside_frame,text="First Name",font=("times new roman",15,"bold" ),bg="white")
        studentID_label.grid(row=0,column=0,padx=15,sticky=W)

        studentID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_fname,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=1,column=0,padx=15,pady=0,sticky=W)

          #student id
        studentname_label=Label(left_inside_frame,text="Last Name",font=("times new roman",15,"bold" ),bg="white")
        studentname_label.grid(row=0,column=1,padx=3,sticky=W)

        studentIname_entry=ttk.Entry(left_inside_frame,textvariable=self.var_lname,width=20,font=("times new roman",12,"bold"))
        studentIname_entry.grid(row=1,column=1,padx=1,pady=0,sticky=W) 

          #contect  
        class_details_label=Label(left_inside_frame,text="Contect",font=("times new roman",15,"bold" ),bg="white")
        class_details_label.grid(row=2,column=0,padx=15,sticky=W)

        class_div_combo=ttk.Entry(left_inside_frame,textvariable=self.var_contect,font=("times new roman",12,"bold" ))
        class_div_combo.grid(row=3,column=0,padx=15,pady=0,sticky=W)
          
          #Email  
        roll_no_label=Label(left_inside_frame,text="Email",font=("times new roman",15,"bold" ),bg="white")
        roll_no_label.grid(row=2,column=1,padx=3,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=3,column=1,padx=1,pady=0,sticky=W)
        #security question
        class_details_label=Label(left_inside_frame,text="Select Security Question",font=("times new roman",15,"bold" ),bg="white")
        class_details_label.grid(row=4,column=0,padx=15,sticky=W)
        class_div_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_securityQ,width=18,font=("times new roman",12,"bold" ),state="readonly")
        class_div_combo["value"]=("Select Question","Your date of birth","birth place","other")
        class_div_combo.current(0)
        class_div_combo.grid(row=5,column=0,padx=15,pady=0,sticky=W)

          # 
        studentname_label=Label(left_inside_frame,text="Security Answer ",font=("times new roman",15,"bold" ),bg="white")
        studentname_label.grid(row=4,column=1,padx=3,sticky=W)

        studentIname_entry=ttk.Entry(left_inside_frame,textvariable=self.var_securityA,width=20,font=("times new roman",12,"bold"))
        studentIname_entry.grid(row=5,column=1,padx=1,pady=0,sticky=W) 

          #class details    
        class_details_label=Label(left_inside_frame,text="Password",font=("times new roman",15,"bold" ),bg="white")
        class_details_label.grid(row=6,column=0,padx=15,sticky=W)

        class_div_combo=ttk.Entry(left_inside_frame,show="*",textvariable=self.var_pass,width=20,font=("times new roman",12,"bold" ))
        class_div_combo.grid(row=7,column=0,padx=15,pady=0,sticky=W)
          
          #roll no    
        roll_no_label=Label(left_inside_frame,text="Confirm Password",font=("times new roman",15,"bold" ),bg="white")
        roll_no_label.grid(row=6,column=1,padx=3,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,show="*",textvariable=self.var_cnpss,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=7,column=1,padx=1,pady=0,sticky=W)
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(left_inside_frame,variable=self.var_check,text="i agree the term & condition",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.grid(row=8,column=0,padx=15,pady=5,sticky=W)

        # buttons==========
        registerbtn=Button(left_inside_frame,command=self.register_data,text="Ragister Now",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        registerbtn.grid(row=15,column=0,padx=15,pady=5,sticky=W)

        loginbtn=Button(left_inside_frame,command=self.register_data,text="Login Now",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.grid(row=15,column=1,padx=0,pady=5,sticky=W)



#==========register function declaration 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityA.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_cnpss.get():
            messagebox.showerror("Error","password not match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please click check button")
        else:
             conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
             my_cursur=conn.cursor()
             sql=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursur.execute(sql,value)
             row=my_cursur.fetchone()
             if row != None:
                messagebox.showerror("Error","user already register , please try another email")
             else:
                my_cursur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_fname.get(),
                                                                    self.var_lname.get(),
                                                                    self.var_contect.get(),
                                                                    self.var_email.get(),
                                                                    self.var_securityQ.get(),
                                                                    self.var_securityA.get(),
                                                                    self.var_pass.get()
                                                                                                         
                                                                                             ))  
             conn.commit()
             conn.close()
             messagebox.showinfo("sucess","values inserted to database")            

if __name__=="__main__":
    root=Tk()
    app=registers(root)
    root.mainloop()        