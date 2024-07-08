import os
import smtplib
from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox as msg
import mysql.connector as sql
import email_pass
import time



class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System ")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="white")

        self.empId = StringVar()
        self.empPass = StringVar()


        # ====================== BACKGROUND IMAGE ====================== #

        self.phone_image=ImageTk.PhotoImage(file=r"D:\PythonProject\assets\3071357.jpg")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=150,y=70)

        # ====================== LOGIN FRAME =========================== #
        login_frames=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frames.place(x=650,y=90,width=350,height=460)

        tittle=Label(login_frames,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=35,y=40)

        lbl_user = Label(login_frames, text="Employee ID ", font=("Andalus", 14),bg="white",fg="#767171")
        lbl_user.place(x=50,y=110)

        txt_employee_id=Entry(login_frames,textvariable=self.empId,font=("Andalus", 15),bg="light grey")
        txt_employee_id.place(x=50,y=150)

        lbl_user = Label(login_frames, text="Password ", font=("Andalus", 14), bg="white", fg="#767171")
        lbl_user.place(x=50, y=200)

        txt_employee_pass = Entry(login_frames, textvariable=self.empPass, font=("Andalus", 15), bg="light grey")
        txt_employee_pass.place(x=50, y=240)

        login = Button(login_frames,text="Log In", command=self.Login, bg="blue", fg="white",
                        font=("times new roman", 12))
        login.place(x=50, y=310, width=230)

        lbl_user = Label(login_frames, text="-----------OR----------", font=("Andalus", 16), bg="white", fg="#767171")
        lbl_user.place(x=70, y=370)

        forget_btn = Button(login_frames, text="Forget Password?",command=self.forget_window, bg="white", fg="black",bd=0,
                       font=("times new roman", 14),activebackground="white")
        forget_btn.place(x=90,y=410,width=170)
        #self.send_email()

    def Login(self):
        Id = self.empId.get()
        Passw = str(self.empPass.get())
        if(Id=="" or Passw==""):
            msg.showerror("Error","Required all fields")
        else:
            try:
                getPass = f"'{Passw}'"
                conn = sql.connect(host="localhost",user="root",password="sajal_23",database="userdb")
                mycursor = conn.cursor()
                mycursor.execute(f"select * from user_detail where id={Id} and password={getPass}")
                gotData = mycursor.fetchone()
                if gotData == None:
                    msg.showerror("Warning","Invalid Id or Password")
                else:
                    msg.showinfo("Success","Successfully Signed In!!")

                conn.commit()
                conn.close()

            except Exception as es:
                msg.showerror("Error",f"Due to {es}")


    def forget_window(self):
        con = sql.connect(host="localhost",user="root",password="sajal_23",database="userdb")
        cur = con.cursor()
        try:
            if self.empId.get()=="":
                msg.showerror('Error',"Employee ID must be required",parent=self.root)
            else:
                cur.execute(f"select email from user_detail where id={self.empId.get()}")
                email=cur.fetchone()
                if email==None:
                    msg.showerror('Error',"Invalid Employee ID,try again",parent=self.root)
                else:
                    # =====Forget WINDOW=====
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    # call send_email_function()

                    self.forget_win = Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    title=Label(self.forget_win,text='Reset Password',font=('goundy old style',15,'bold'),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email ", font=("times new roman",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg='lightyellow')
                    txt_reset.place(x=20,y=100,width=250,height=30)
                    self.btn_reset = Button(self.forget_win, text="SUBMIT", font=("times new roman", 15),
                                                bg='lightblue')
                    self.btn_reset.place(x=280, y=100, width=100, height=30)

                    lbl_new_pass = Label(self.forget_win, text="New Password", font=('times new roman', 15)).place(x=20,y=160)

                    txt_new_pass = Label(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=190,width=250,height=30)

                    lbl_c_pass = Label(self.forget_win, text='Confirm Password', font=('times new roman',15)).place(x=20,y=225)

                    txt_c_pass = Label(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg='lightyellow').place(x=20,y=255,width=250,height=30)
                    self.btn_update = Button(self.forget_win, text="Update", state=DISABLED,font=("times new roman", 15),
                                                bg='lightblue')
                    self.btn_update.place(x=150, y=300, width=100, height=30)


        except Exception as ex:
            msg.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    #def send_email(self):
        #s = smtplib.SMTP('smtp.gmail.com',587)
        # s.starttls()
        # email_ = email_pass.email_
        # pass_ = email_pass.pass_
        #
        # s.login(email_,pass_)

       # self.otp = str(time.strftime('%H%M%S'))+str(time.strftime('%S'))
        #print(self.otp)





if __name__ == "__main__":
    root=Tk()
    obj=Login(root)

    root.mainloop()




