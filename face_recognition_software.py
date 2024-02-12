from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import cv2
from PIL import Image,ImageTk
from student import Student
#
# from new.update import Student
from train import train
from attendence import attendence
from developer import developer
from main import face_recognition_system

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root): 
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x1500+0+0")
        

        self.bg=ImageTk.PhotoImage(file=r"D:\attendence management software\PHOTO\loginimage.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=100,width=300,height=400)

        img1=Image.open(r"D:\attendence management software\PHOTO\licon1.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(image=self.photoimg1,bg="black",borderwidth=0)
        bg_img.place(x=610,y=120,width=70,height=70)

        get_str=Label(frame,text="Get started",font=("times new roman",15,"bold"),fg="white",bg="black")
        get_str.place(x=93,y=90)

        username=Label(frame,text="UserName :-",font=("times new roman",10,"bold"),fg="white",bg="black")
        username.place(x=40,y=150)
        
        self.txtuser=StringVar()
        self.txtpass=StringVar()

        self.textuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",12,"bold"))
        self.textuser.place(x=113,y=150,height=20)

        userpsw=Label(frame,text="Password :-",font=("times new roman",10,"bold"),fg="white",bg="black")
        userpsw.place(x=40,y=190)

        self.userpsw=ttk.Entry(frame,show="*",textvariable=self.txtpass,font=("times new roman",12,"bold"))
        self.userpsw.place(x=113,y=190,height=20)

        # icon images
        img2=Image.open(r"D:\attendence management software\PHOTO\usericon1.jpg")
        img2=img2.resize((20,20),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        bg_img=Label(image=self.photoimg2,bg="black",borderwidth=0)
        bg_img.place(x=510,y=245,width=30,height=30)

        img3=Image.open(r"D:\attendence management software\PHOTO\pwd.jpg")
        img3=img3.resize((20,20),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(image=self.photoimg3,bg="black",borderwidth=0)
        bg_img.place(x=510,y=285,width=30,height=30)

#login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=100,y=250,width=100,height=30)

 #===new user register
        newuser=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),bg="black",fg="white",borderwidth=0,relief=RIDGE,activeforeground="white",activebackground="black")
        newuser.place(x=10,y=300,width=150,height=20)

#=======forget password
        forget=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),bg="black",fg="white",borderwidth=0,relief=RIDGE,activeforeground="white",activebackground="black")
        forget.place(x=10,y=320,width=150,height=20) 
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fiels are require")
        elif self.txtuser.get()=="abdul" and self.txtpass.get()=="1234":
             messagebox.showinfo("Succcess","welcome")
        else:
             conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
             my_cursur=conn.cursor()
             my_cursur.execute("select * from register where email=%s and password=%s" ,(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpass.get()                                                     
                                                                                                        ))
             row=my_cursur.fetchone()
             if row == None:
                 messagebox.showerror("Error","invalid data ",parent=self.root)
             else:
                 open_main=messagebox.askyesno("YesNo","acess only admin")
                 if open_main>0:
                     self.new_window=Toplevel(self.root)
                     self.app=face_recognition_system(self.new_window)
                     
                 else:
                     if not open_main:
                         return    
             conn.commit()
             self.clear()   
             conn.close() 
                 
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")       
 #===========reset password window
    
    
 # forgot password window========   
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
            my_cursur=conn.cursor()
            sql=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursur.execute(sql,value)
            row=my_cursur.fetchone()
            #print(row)
            if row == None:
                messagebox.showerror("Error","Enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("300x400+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",12,"bold"),bg="blue",fg="white")
                l.place(x=0,y=0,relwidth=1)

                securityQ=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold" ))
                securityQ.place(x=45,y=50)

                self.combo_securityQ=ttk.Combobox(self.root2,font=("times new roman",12,"bold" ),state="readonly")
                self.combo_securityQ["values"]=("select","your date of birth","birth place","other")
                self.combo_securityQ.place(x=45,y=80,width=204)
                self.combo_securityQ.current(0)

                securityA=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold" ))
                securityA.place(x=45,y=110)

                self.text_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.text_security.place(x=45,y=140)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold" ))
                new_password.place(x=45,y=180)

                self.txt_newpass=ttk.Entry(self.root2,show="*",font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=45,y=205)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=70,y=260,width=150)

                copy_right=Label(self.root2,text="© 2023 Copy_Right. All Rights Reserved.",font=("times new roman",8,"bold" ),fg="blue")
                copy_right.place(x=35,y=370)  

    def reset_pass(self):
        if self.combo_securityQ.get()=="select" or self.text_security.get()=="" or self.txt_newpass.get()=="":
           messagebox.showerror("Error","fill the all field")
       
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="1234@",database="facerecognition")
                my_cursur=conn.cursor()
                sqls=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_securityQ.get(),self.text_security.get())
                my_cursur.execute(sqls,value)
                row=my_cursur.fetchone()
                if row == None:
                    messagebox.showerror("Error","please enter the currect answer",parent=self.root2)
                else:
                    sql=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    my_cursur.execute(sql,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your password has been reset, please login new passwoed",parent=self.root)
                    self.root2.destroy()
                    self.textuser.focus()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root2)
    
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x1500+0+0")
        self.root.title("Register")
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
        confirm_pass_label=Label(left_inside_frame,text="Confirm Password",font=("times new roman",15,"bold" ),bg="white")
        confirm_pass_label.grid(row=6,column=1,padx=3,sticky=W)

        confirm_pass_entry=ttk.Entry(left_inside_frame,show="*",textvariable=self.var_cnpss,width=20,font=("times new roman",12,"bold"))
        confirm_pass_entry.grid(row=7,column=1,padx=1,pady=0,sticky=W)
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(left_inside_frame,variable=self.var_check,text="i agree the term & condition",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.grid(row=8,column=0,padx=15,pady=5,sticky=W)

        # buttons==========
        registerbtn=Button(left_inside_frame,command=self.register_data,text="Ragister Now",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        registerbtn.grid(row=15,column=0,padx=15,pady=5,sticky=W)

        loginbtn=Button(left_inside_frame,command=self.return_login,text="Login Now",width=20,font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.grid(row=15,column=1,padx=0,pady=5,sticky=W)



#==========register function declaration 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityA.get()=="select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
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
             if row!=None:
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
    def return_login(self):
        self.root.destroy()           

if __name__=="__main__":
    main()
     