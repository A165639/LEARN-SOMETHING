from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x600+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_fucn)

        main_frame=Frame(self.root,bd=3,bg="powder blue",width=600)
        main_frame.pack()

        img_chat=Image.open(r"D:\attendence management software\PHOTO\chat.jpg")
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_lbl=Label(main_frame,bd=3,relief=RIDGE,anchor='nw',width=610,height=60,compound=LEFT,image=self.photoimg,text='Chat Me',font=('arial',30,'bold'),fg='green',bg='white')
        Title_lbl.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=5,relief=RIDGE,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=3,bg="white",width=630)
        btn_frame.pack()

        lbl_1=Label(btn_frame,text="type something",font=("arial",13,'bold'),fg="green",bg='white')
        lbl_1.grid(row=0,column=0,padx=2,pady=2,sticky=W)

      
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=30,font=('times new roman',13,'bold'))
        self.entry1.grid(row=0,column=1,padx=2,sticky=W)

        self.send=Button(btn_frame,command=self.send,text="send",font=('times new roman',13,'bold'),width=5,bg="green")
        self.send.grid(row=0,column=2,padx=2,sticky=W)

        self.Clear=Button(btn_frame,command=self.clear,text="Clear",font=('times new roman',13,'bold'),width=10,bg="green")
        self.Clear.grid(row=1,column=0,padx=2,sticky=W)

        self.msg=''
        self.lbl_11=Label(btn_frame,text=self.msg,width=20,font=("arial",13,'bold'),fg="red",bg='white')
        self.lbl_11.grid(row=1,column=1,padx=2,sticky=W)


#  function ===============
    def enter_fucn(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set()    

    def send(self):
        send='\t'+'you- '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg="please enter some input"
            self.lbl_11.config(text=self.msg,fg='red')
        else:
            self.msg=''  
            self.lbl_11.config(text=self.msg,fg='red')

        if (self.entry.get()=='hello'): 
           self.text.insert(END,'\n'+'Bot - Hi')

        elif (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot - Hello')  

        elif (self.entry.get()=='How are you'):
            self.text.insert(END,'\n\n'+'Bot - Find and you') 

        elif (self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot - Nice to hear') 

        elif (self.entry.get()=='Who Create You'):
            self.text.insert(END,'\n\n'+'Bot - Abdul Mannan did using Pthon with tkinter') 

        elif (self.entry.get()=='What is your name' or self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot - My name is Bot') 

        elif (self.entry.get()=='Can you speak Hindi'):
            self.text.insert(END,'\n\n'+"Bot - I'm  still learning it..") 

        elif (self.entry.get()=='what is machine learning?'):
            self.text.insert(END,'\n\n'+'Bot - machine learning is a branch/nof artificial intelligence (AI)')
                                                      
        elif (self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot - thank u for chatting') 

        elif (self.entry.get()==''):
            self.text.insert(END,'\n\n'+'Bot - please enter some input')     

        else:
            self.text.insert(END,'\n\n'+"Bot - Sorry i did'nt get it..")     

if __name__=="__main__":
    root=Tk()
    app=Chatbot(root)
    root.mainloop()     
