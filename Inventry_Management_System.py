from tkinter import *
from PIL import Image, ImageTk
from EMployee import Employeclass
from Supplier import Supplierclass
from category import Categoryclass
from product import Productclass
from Sales import Salesclass
from tkinter import messagebox
import mysql.connector as mysql
import os
import time


class IMS:

    def __init__(self, root):
        self.new_obj = None
        self.new_win = None
        self.root = root
        self.root.geometry("1533x800+0+0")
        self.root.title("Inventory Management System ")
        # { Background color }
        self.root['bg'] = '#483d8b'
        self.root.state("zoomed")

        # =============================[  Add_image_left_menu ]=========================================================
        self.left_img = Image.open("image/img_3.png")
        self.left_img = self.left_img.resize((325, 280))
        self.left_img = ImageTk.PhotoImage(self.left_img)
        # :::::::::::::::::::::::::::::::::::[ Employee_logo_image ]::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.emp_img = Image.open("image/img.png")
        self.emp_img = self.emp_img.resize((200, 130))
        self.emp_img = ImageTk.PhotoImage(self.emp_img)

        # =============================[  supplier_logo_mage ]==========================================================


        self.supp_img = Image.open("image/img_4.png")
        self.supp_img = self.supp_img.resize((190, 120))
        self.supp_img = ImageTk.PhotoImage(self.supp_img)

        # =============================[ Category logo image ]==========================================================

        self.cat_img = Image.open("image/img_5.png")
        self.cat_img = self.cat_img.resize((190, 120))
        self.cat_img = ImageTk.PhotoImage(self.cat_img)

        # =============================[  Product logo image ]==========================================================

        self.pro_img = Image.open("image/img_6.png")
        self.pro_img = self.pro_img.resize((190, 120))
        self.pro_img = ImageTk.PhotoImage(self.pro_img)

        # =============================[ Sales logo image ]=============================================================

        self.sale_img = Image.open("image/img_7.png")
        self.sale_img = self.sale_img.resize((190, 120))
        self.sale_img = ImageTk.PhotoImage(self.sale_img)

        # =============================[ Menu Details ]=================================================================

        # =============================[ shopping icon resizing ]=======================================================

        image = Image.open("image/shopping-cart.png")
        resize1 = image.resize((60, 60))
        self.photo = ImageTk.PhotoImage(resize1)

        # =============================[ title ]========================================================================

        title = Label(self.root, image=self.photo, compound="left", text="Inventory Management system",
                      font=("times new roman", 40, "bold"), anchor="sw", padx=20, bg="#000c69", fg="white")
        title.place(x=0, y=0, relwidth=1.0, height=70)
        # ===============================[ Button  ]====================================================================

        b1 = Button(self.root, text="Logout", cursor="hand2", font=("arial", 15, "bold"), bg="yellow")
        b1.place(x=1400, y=10)

        b2 = Button(self.root, text="Refresh", cursor="hand2", command=self.refresh, font=("arial", 15, "bold"),
                    bg="yellow")
        b2.place(x=1300, y=10)
        # ==============================================================================================================
        # =============================[ Clock ]========================================================================

        self.clock = Label(self.root, text="Welcome to Inventory\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                           font=("times new roman", 15), padx=20, bg="gray", fg="white")
        self.clock.place(x=0, y=70, relwidth=1.0, height=30)

        # =============================[  Menu ]========================================================================

        self.button_symbol = Image.open("image/OIP.png")
        self.button_symbol = self.button_symbol.resize((20, 20))
        self.button_symbol = ImageTk.PhotoImage(self.button_symbol)

        B1 = Button(self.root, text="Employee", anchor="w", font=("arial", 18, "bold"), bg="#bf94e4", fg="black",
                    image=self.button_symbol, cursor="hand2", bd=3, compound="left", command=self.Employee)
        B1.place(x=150, y=360, width=300)

        B2 = Button(self.root, text="Supplier", image=self.button_symbol, command=self.Supplier, compound="left",
                    anchor="w", font="arial 18 bold", bg="#bf94e4", fg="black", cursor="hand2", bd=3)
        B2.place(x=650, y=360, width=300)

        B3 = Button(self.root, text="Category", image=self.button_symbol, command=self.Category, compound="left",
                    anchor="w", font="arial 18 bold", bg="#bf94e4", fg="black", cursor="hand2", bd=3)
        B3.place(x=1150, y=360, width=300)

        B4 = Button(self.root, text="Products", image=self.button_symbol, command=self.Product, compound="left",
                    anchor="w", font="arial 18 bold", bg="#bf94e4", fg="black", cursor="hand2", bd=3)
        B4.place(x=150, y=650, width=300)

        B5 = Button(self.root, text="Sales", image=self.button_symbol, command=self.Sales, compound="left",
                    anchor="w", font="arial 18 bold", bg="#bf94e4", fg="black", cursor="hand2", bd=3)
        B5.place(x=650, y=650, width=300)

        B6 = Button(self.root, text="Exit", image=self.button_symbol, command=self.Exit, compound="left", anchor="w",
                    font="arial 18 bold", bg="#bf94e4", fg="black", cursor="hand2", bd=3)
        B6.place(x=1150, y=650, width=300)

        # ===============================[ Menu Details]================================================================

        total_count = self.count()
        self.Emp_label = Label(self.root, image=self.emp_img, compound="top", anchor="n", pady=5,
                               font=("Stencil Std", 15, "bold"), bd=5, bg="#734f96", fg="#fdf5e6", relief=RIDGE)

        self.Emp_label.place(x=150, y=160, height=200, width=300)

        self.Emp_label.configure(text=f"Total Employee\n[{total_count[0]}]")

        self.Supp_label = Label(self.root, image=self.supp_img, compound="top", font=("Stencil Std", 15, "bold"), bd=5,
                                bg="#734f96", fg="#fdf5e6", relief=RIDGE)

        self.Supp_label.place(x=650, y=160, height=200, width=300)
        self.Supp_label.configure(text=f"Total Supplier\n[{total_count[1]}] ")

        self.Cat_label = Label(self.root, image=self.cat_img, compound="top", font=("Stencil Std", 15, "bold"), bd=5,
                               bg="#734f96", fg="#fdf5e6", relief=RIDGE)

        self.Cat_label.place(x=1150, y=160, height=200, width=300)
        self.Cat_label.configure(text=f"Total Category\n[{total_count[2]}]")

        self.Pro_label = Label(self.root, image=self.pro_img, compound="top", font=("Stencil Std", 15, "bold"), bd=5,
                               bg="#734f96", fg="#fdf5e6", relief=RIDGE)
        self.Pro_label.place(x=150, y=450, height=200, width=300)

        self.Pro_label.configure(text=f"Total Category\n[{total_count[3]}] ")

        self.Sal_label = Label(self.root, image=self.sale_img, compound="top", font=("Stencil Std", 15, "bold"), bd=5,
                               bg="#734f96", fg="#fdf5e6", relief=RIDGE)

        self.Sal_label.place(x=650, y=450, height=200, width=300)
        self.Sal_label.configure(text=f"Total Sales\n[{len(os.listdir('Bill'))}] ")

        self.Exit_label = Label(self.root, text="Exit", compound="top", font=("Stencil Std", 50, "bold"), bd=5,
                                bg="#734f96", fg="black", relief=RIDGE)

        self.Exit_label.place(x=1150, y=450, height=200, width=300)
        # self.refresh()
        # self.count()

        # =============================[ Footer ]=======================================================================
        footer = Label(self.root, text="IMS | Inventory management system \n for any technical issue contact us: "
                                       "+91 76XXXXXXXX", font=("times new roman", 10), padx=20, bg="gray", fg="white")
        footer.place(x=0, y=745, relwidth=1.0, height=60)

        # ==============================================================================================================

        # =============================[ Function ]=====================================================================

        self.refresh()

    def Employee(self):

        self.new_win = Toplevel(self.root)
        self.new_obj = Employeclass(self.new_win)

    def Supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Supplierclass(self.new_win)

    def Category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Categoryclass(self.new_win)

    def Product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Productclass(self.new_win)

    def Sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Salesclass(self.new_win)

    def count(self):
        table = ["Employee", "Supplier", "Category", "Product"]
        no_of_count = []
        conn = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = conn.cursor()
        try:
            for i in table:
                cur.execute(f"SELECT count(*) FROM {i}  ")

                count = cur.fetchone()[0]
                no_of_count.append(count)

            return no_of_count


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)
        finally:
            if conn:
                conn.close()

    def refresh(self):

        total_count = self.count()
        self.Emp_label.configure(text=f"Total Employee\n[{total_count[0]}] ")
        self.Supp_label.configure(text=f"Total Supplier\n[{total_count[1]}] ")
        self.Cat_label.configure(text=f"Total Category\n[{total_count[2]}]")
        self.Sal_label.configure(text=f"Total Sales\n[{len(os.listdir('Bill'))}] ")
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.clock.configure(text=f"Welcome to Inventory\t\t Date:{date_}\t\t Time:{time_}")
        self.clock.after(200, self.refresh)

    def Exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)

    root.mainloop()
