from tkinter import *
from tkinter import messagebox
from EMployee import Employeclass
from Biling import Bill_class
from PIL import ImageTk,Image
import mysql.connector as mysql


from Inventry_Management_System import IMS  # Import the InventoryManagementSystem class

class LoginSystem:
    def __init__(self, root):
        self.new_obj = None
        self.new_win = None
        self.root = root
        self.root.geometry("1533x800+0+0")
        self.root.title("Inventory Management System ")
        # { Background color }
        self.root['bg'] = 'white'
        self.root.state("zoomed")

        self.userId = StringVar()
        self.password = StringVar()

        # =====image====
        self.bg_img = Image.open("image/3071357.jpg")
        self.bg_img = self.bg_img.resize((500, 500))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)



        # === Entry Frame ===

        self.phone_image = ImageTk.PhotoImage(file="D:/Pycharm/ProjectFile/Inventory Management System/image"
                                                   "/3071357.jpg")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=300, y=100)

        # ====================== LOGIN FRAME =========================== #
        login_frames = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frames.place(x=800, y=110, width=350, height=460)

        tittle = Label(login_frames, text="Login System", font=("Elephant", 30, "bold"), bg="white").place(x=35, y=40)

        lbl_user = Label(login_frames, text="Emp/Admin ID ", font=("Andalus", 14), bg="white", fg="#767171")
        lbl_user.place(x=50, y=110)

        txt_employee_id = Entry(login_frames, textvariable=self.userId, font=("Andalus", 15), bg="light grey")
        txt_employee_id.place(x=50, y=150)

        lbl_user = Label(login_frames, text="Password ", font=("Andalus", 14), bg="white", fg="#767171")
        lbl_user.place(x=50, y=200)

        txt_employee_pass = Entry(login_frames, textvariable=self.password, font=("Andalus", 15), bg="light grey")
        txt_employee_pass.place(x=50, y=240)

        login = Button(login_frames, text="Log In", command=self.login, bg="blue", fg="white",
                       font=("times new roman", 12))
        login.place(x=50, y=310, width=230)

        lbl_user = Label(login_frames, text="-----------OR----------", font=("Andalus", 16), bg="white", fg="#767171")
        lbl_user.place(x=70, y=370)

        forget_btn = Button(login_frames, text="Forget Password?",command=self.info, bg="white", fg="black",
                            bd=0,
                            font=("times new roman", 14), activebackground="white")
        forget_btn.place(x=90, y=410, width=170)
        # self.send_email()



    def login(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:

            # Ask if the user is an admin
            yes = messagebox.askyesno('Confirm', 'Are you admin?', parent=self.root)

            if yes:


                valid_username = "1001"
                valid_password = "admin123"


                entered_userId = self.userId.get()
                entered_password = self.password.get()
                if entered_userId == "" or entered_password == "":
                    messagebox.showinfo("Error","please enter admin id and password")

                elif entered_userId == valid_username and entered_password == valid_password:
                    messagebox.showinfo("Login Successful", "Welcome, Admin!")
                    self.root.destroy()
                    self.open_inventory_management_system()
                else:
                    messagebox.showerror("Login Failed", "Invalid username or password")
            else:
                entered_userId = self.userId.get()
                entered_password = self.password.get()

                if entered_userId == "" or entered_password == "":
                    messagebox.showinfo("Info", "All fields are required", parent=self.root)
                else:

                    cur.execute("SELECT * FROM Employee WHERE Eid=%s AND Pass=%s",
                                (entered_userId, entered_password))
                    getdata = cur.fetchone()

                    if getdata is None:
                        messagebox.showerror('Warning', "Invalid Id and Password")
                    else:
                        messagebox.showinfo('Success', "Successfully Signed in")
                        self.root.destroy()
                        self.open_Billing()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()


    def open_inventory_management_system(self):
        root_inventory = Tk()
        inventory_system = IMS(root_inventory)
        root_inventory.mainloop()

    def open_Billing(self):
        root_bill = Tk()
        Bill_system = Bill_class(root_bill)
        root_bill.mainloop()

    # def forget_pass(self):
    #     con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
    #     cur = con.cursor()
    #     try:
    #         if self.userId.get() == "":
    #             messagebox.showerror('Error',"Please enter userId")
    #         else:
    #             cur.execute("SELECT * FROM Employee WHERE Eid=%",(us))


    def info(self):
        messagebox.showinfo("Working", " Work in Progress")

if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()
