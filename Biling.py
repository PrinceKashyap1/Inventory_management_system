from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector as mysql
import os
import tempfile
import time


class Bill_class:

    def __init__(self, root):
        self.new_obj = None
        self.new_win = None
        self.root = root
        self.root.geometry("1533x800+0+0")
        self.root.title("Inventory Management System ")
        self.root['bg'] = "lightGrey"
        # =============================[ Variable ]=====================================================================
        self.var_search = StringVar()
        self.var_contact = StringVar()
        self.var_pid = StringVar()
        self.var_pro_name = StringVar()
        self.var_cust_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.var_stock = StringVar()
        self.varCal_in = StringVar()
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()
        self.cart_list = []
        self.chk_print = 0

        # =============================[ Clock ]========================================================================

        self.clock = Label(self.root, text="Welcome to Inventory\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                           font=("times new roman", 15), padx=20, bg="gray", fg="white")
        self.clock.place(x=0, y=70, relwidth=1.0, height=30)

        # =============================[ shopping icon Resizing ]=======================================================

        image = Image.open("image/shopping-cart.png")
        resize1 = image.resize((60, 60))
        self.photo = ImageTk.PhotoImage(resize1)

        # =============================[ title ]========================================================================

        title = Label(self.root, image=self.photo, compound="left", text="Inventory Management system",
                      font=("times new roman", 40, "bold"), anchor="sw", padx=20, bg="#000c69", fg="white")
        title.place(x=0, y=0, relwidth=1.0, height=70)
        # ===============================[ Button ]=====================================================================

        b1 = Button(self.root, text="Logout", cursor="hand2", font=("arial", 15, "bold"), bg="yellow")
        b1.place(x=1400, y=10)

        # ===============================[ Product Frame ]==============================================================
        #   [ Product Frame1 ]==========================================================================================

        pro_frame1 = Frame(self.root, bd=4, bg="white", relief=RIDGE)
        pro_frame1.place(x=6, y=110, width=410, height=550)

        #   [ Product Frame2 ]==========================================================================================
        pro_frame2 = Frame(pro_frame1, bd=4, bg="white", relief=RIDGE)
        pro_frame2.place(x=2, y=42, width=398, height=90)

        #   [ Product Frame3 ]==========================================================================================
        Pro_frame3 = Frame(pro_frame1, bd=3, bg="white", relief=RIDGE)
        Pro_frame3.place(x=2, y=140, width=400, height=370)

        # =[ Label ]====================================================================================================

        pro_title = Label(pro_frame1, text="All Product", font=("gaudy old style", 20, "bold"), bg="#262626",
                          fg="white")
        pro_title.pack(fill=X, side=TOP)

        search_lbl = Label(pro_frame2, text="Search Product | by Name", font=("times new roman", 15, "bold"),
                           bg="white",
                           fg="green")
        search_lbl.place(x=2, y=5)

        S_name_lbl = Label(pro_frame2, text="Product Name", font=("times new roman", 15, "bold"),
                           bg="white")
        S_name_lbl.place(x=5, y=45)

        S_name_txt = Entry(pro_frame2, textvariable=self.var_search, font=("times new roman", 15, "bold"),
                           bg="lightYellow")
        S_name_txt.place(x=130, y=47, width=150, height=22)

        ALL_Show_btn = Button(pro_frame2, text="Show All", command=self.show, cursor="hand2",
                              font=("arial", 15, "bold"), bg="black",
                              fg="white")
        ALL_Show_btn.place(x=285, y=10, width=100, height=25)

        P_Search_btn = Button(pro_frame2, text="Search", command=self.search, cursor="hand2",
                              font=("arial", 15, "bold"),
                              bg="yellow")
        P_Search_btn.place(x=284, y=45, width=100, height=25)

        # =[ Product details ]==========================================================================================

        scroll_x = Scrollbar(Pro_frame3, orient=HORIZONTAL)
        scroll_y = Scrollbar(Pro_frame3, orient=VERTICAL)

        self.pro_table = ttk.Treeview(Pro_frame3, columns=("Pid", "Name", "Price", "QTY", "Status"),
                                      yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        # self.supp_table.bind("<ButtonRelease-1>", self.get_data)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.pro_table.xview)
        scroll_y.config(command=self.pro_table.yview)
        # ===============================[  Heading ]===================================================================

        self.pro_table.heading("Pid", text="Pid")
        self.pro_table.heading("Name", text="Name")
        self.pro_table.heading("Price", text="price")
        self.pro_table.heading("QTY", text="QTY")
        self.pro_table.heading("Status", text="Status")

        self.pro_table["show"] = "headings"

        self.pro_table.column("Pid", width=40)
        self.pro_table.column("Name", width=90)
        self.pro_table.column("Price", width=90)
        self.pro_table.column("QTY", width=50)
        self.pro_table.column("Status", width=50)

        self.pro_table.pack(fill=BOTH, expand=1)

        self.pro_table.bind("<ButtonRelease-1>", self.get_data)
        Note_lbl = Label(Pro_frame3, text="Enter 0 quantity to remove Product from the Cart", font=("gaudy old style",
                                                                                                    10), fg="red",
                         bg="white")
        Note_lbl.pack(fill=X, side=BOTTOM)

        # self.show()

        # ========================================[ Customer Frame ]====================================================

        cust_frame = Frame(self.root, bd=4, bg="white", relief=RIDGE)
        cust_frame.place(x=420, y=110, width=530, height=70)




        # =[ Customer Label ]===========================================================================================




        pro_title = Label(cust_frame, text="Customer Details", font=("gaudy old style", 15, "bold"), bg="#8c92ac",
                          fg="white")
        pro_title.pack(fill=X, side=TOP)

        cust_name_lbl = Label(cust_frame, text="Name", font=("times new roman", 15, "bold"),
                              bg="white")
        cust_name_lbl.place(x=5, y=35)

        cust_contact_lbl = Label(cust_frame, text="Contact", font=("times new roman", 15, "bold"),
                                 bg="white")
        cust_contact_lbl.place(x=270, y=35)



        # =[ Customer text ]============================================================================================


        cust_name_txt = Entry(cust_frame, textvariable=self.var_cust_name, font=("times new roman", 15, "bold"),
                              bg="lightYellow")
        cust_name_txt.place(x=80, y=35, width=180)

        cust_contact_txt = Entry(cust_frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"),
                                 bg="lightYellow")
        cust_contact_txt.place(x=380, y=35, width=140)


        # ========================================[ Calculator or cart Frame ]==========================================

        cal_cart_frame = Frame(self.root, bd=4, bg="white", relief=RIDGE)
        cal_cart_frame.place(x=420, y=190, width=530, height=360)

        cal_frame = Frame(cal_cart_frame, bd=4, bg="white", relief=RIDGE)
        cal_frame.place(x=5, y=10, width=268, height=340)

        #   [ Product Frame3 ]==========================================================================================
        Cart_frame = Frame(cal_cart_frame, bd=3, bg="white", relief=RIDGE)
        Cart_frame.place(x=280, y=8, width=245, height=340)

        scroll_x = Scrollbar(Cart_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Cart_frame, orient=VERTICAL)

        self.Cart_table = ttk.Treeview(Cart_frame, columns=("pid", "Name", "Price", "QTY"),
                                       yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        # self.supp_table.bind("<ButtonRelease-1>", self.get_data)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cart_table.xview)
        scroll_y.config(command=self.Cart_table.yview)
        # ===============================[  Heading ]===================================================================

        self.Cart_table.heading("pid", text="Pid")
        self.Cart_table.heading("Name", text="Name")
        self.Cart_table.heading("Price", text="price")
        self.Cart_table.heading("QTY", text="QTY")

        self.Cart_table["show"] = "headings"

        self.Cart_table.column("pid", width=40)
        self.Cart_table.column("Name", width=100)
        self.Cart_table.column("Price", width=90)
        self.Cart_table.column("QTY", width=40)
        self.Cart_table.pack(fill=BOTH, expand=1)
        self.Cart_table.bind("<ButtonRelease-1>", self.get_data_cart)

        cart_lbl = Label(Cart_frame, text="Cart \t total Product: [0]", font=("gaudy old style", 10),
                         bg="lightGrey")
        cart_lbl.pack(fill=X, side=TOP)


        # =[ Cart Widgets Frame ]===================================================================


        Cart_wid_frame = Frame(self.root, bd=3, bg="white", relief=RIDGE)
        Cart_wid_frame.place(x=420, y=550, width=530, height=110)

        prod_name_lbl = Label(Cart_wid_frame, text="Name", font=("times new roman", 15, "bold"),
                              bg="white")
        prod_name_lbl.place(x=5, y=5)

        prod_name_txt = Entry(Cart_wid_frame, textvariable=self.var_pro_name, font=("times new roman", 15, "bold"),
                              state='readonly',
                              bg="lightYellow")
        prod_name_txt.place(x=5, y=35, width=190, height=22)

        prod_price_lbl = Label(Cart_wid_frame, text="Price per QTY", font=("times new roman", 15, "bold"),
                               bg="white")
        prod_price_lbl.place(x=230, y=5)

        prod_price_txt = Entry(Cart_wid_frame, textvariable=self.var_price, font=("times new roman", 15, "bold"),
                               state='readonly',
                               bg="lightYellow")
        prod_price_txt.place(x=230, y=35, width=150, height=22)

        prod_QTY_lbl = Label(Cart_wid_frame, text="Quantity", font=("times new roman", 15, "bold"),
                             bg="white")
        prod_QTY_lbl.place(x=390, y=5)

        prod_QTY_txt = Entry(Cart_wid_frame, textvariable=self.var_qty, font=("times new roman", 15, "bold"),

                             bg="lightYellow")
        prod_QTY_txt.place(x=390, y=35, width=120, height=22)

        self.In_stock_lbl = Label(Cart_wid_frame, text="In Stock", font=("times new roman", 15, "bold"),
                                  bg="white")
        self.In_stock_lbl.place(x=5, y=70)

        Clear_btn = Button(Cart_wid_frame, text="Clear",command=self.clear_cart, font=("times new roman", 15, "bold"), cursor="hand2",
                           bg="lightGrey", relief=RIDGE)
        Clear_btn.place(x=180, y=70, width=150, height=30)

        Add_update_btn = Button(Cart_wid_frame, text="Add | Update", command=self.add_update_cart,
                                font=("times new roman", 15, "bold"), cursor="hand2",
                                bg="orange", relief=RIDGE)
        Add_update_btn.place(x=340, y=70, width=180, height=30)



     # ===============================[ Calculator Frame ]===========================================================


        self.txt_cal_in = Entry(cal_frame, textvariable=self.varCal_in, font=("arial", 15, "bold"), width=22, bd=9,
                                justify=RIGHT, relief=GROOVE)
        self.txt_cal_in.grid(row=0, columnspan=4)

        self.val = IntVar()
        btn_7 = Button(cal_frame, text="7", font=("arial", 15, "bold"), command=lambda: self.get_input(7), bd=5,
                       width=4,
                       pady=13, cursor="hand2")
        btn_8 = Button(cal_frame, text="8", font=("arial", 15, "bold"), command=lambda: self.get_input(8), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_9 = Button(cal_frame, text="9", font=("arial", 15, "bold"), command=lambda: self.get_input(9), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_plus = Button(cal_frame, text="+", font=("arial", 15, "bold"), command=lambda: self.get_input('+'), bd=5,
                          width=4, pady=13, cursor="hand2")

        btn_4 = Button(cal_frame, text="4", font=("arial", 15, "bold"), command=lambda: self.get_input(4), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_5 = Button(cal_frame, text="5", font=("arial", 15, "bold"), command=lambda: self.get_input(5), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_6 = Button(cal_frame, text="6", font=("arial", 15, "bold"), command=lambda: self.get_input(6), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_minus = Button(cal_frame, text="-", font=("arial", 15, "bold"), command=lambda: self.get_input('-'), bd=5,
                           width=4, pady=13, cursor="hand2")

        btn_1 = Button(cal_frame, text="1", font=("arial", 15, "bold"), command=lambda: self.get_input(1), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_2 = Button(cal_frame, text="2", font=("arial", 15, "bold"), command=lambda: self.get_input(2), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_3 = Button(cal_frame, text="3", font=("arial", 15, "bold"), command=lambda: self.get_input(3), bd=5,
                       width=4, pady=13, cursor="hand2")
        btn_into = Button(cal_frame, text="*", font=("arial", 15, "bold"), command=lambda: self.get_input('*'), bd=5,
                          width=4, pady=13, cursor="hand2")

        btn_zero = Button(cal_frame, text="0", font=("arial", 15, "bold"), command=lambda: self.get_input(0), bd=5,
                          width=4, pady=13, cursor="hand2")
        btn_c = Button(cal_frame, text="c", bg="#4169e1", fg="white", font=("arial", 15, "bold"), command=self.clear,
                       bd=5, width=4, pady=13, cursor="hand2")
        btn_equal = Button(cal_frame, text="=", bg="#8fbc8f", fg="white", font=("arial", 15, "bold"),
                           command=self.perform, bd=5, width=4, pady=13, cursor="hand2")
        btn_div = Button(cal_frame, text="/", font=("arial", 15, "bold"), command=lambda: self.get_input('/'), bd=5,
                         width=4, pady=13, cursor="hand2")

        btn_7.grid(row=1, column=0)
        btn_8.grid(row=1, column=1)
        btn_9.grid(row=1, column=2)
        btn_plus.grid(row=1, column=3)

        btn_4.grid(row=2, column=0)
        btn_5.grid(row=2, column=1)
        btn_6.grid(row=2, column=2)
        btn_minus.grid(row=2, column=3)

        btn_1.grid(row=3, column=0)
        btn_2.grid(row=3, column=1)
        btn_3.grid(row=3, column=2)
        btn_into.grid(row=3, column=3)

        btn_zero.grid(row=4, column=0)
        btn_equal.grid(row=4, column=1)
        btn_c.grid(row=4, column=2)
        btn_div.grid(row=4, column=3)

        # ===============================[ Billing area frame ]=========================================================
        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=953, y=110, width=410, height=410)

        bill_title = Label(bill_frame, text="Customer Bill Area", font=("gaudy old style", 20, "bold"), bg="#c4c3d0",
                           fg="white")
        bill_title.pack(fill=X, side=TOP)

        scroll_y = Scrollbar(bill_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(bill_frame, yscrollcommand=scroll_y.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_bill_area.yview)

        # ===============================[ Billing Button ]=============================================================
        bill_menu_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_menu_frame.place(x=953, y=520, width=410, height=140)

        self.amount_lbl = Label(bill_menu_frame, text="Bill Amount\n[0]", font=("gaudy old style", 11, "bold"),
                                bg="#3f51b5",
                                 fg="white")
        self.amount_lbl.place(x=2, y=5, width=120, height=70)
        self.discount_lbl = Label(bill_menu_frame, text="Discount\n[5%]", font=("gaudy old style", 12, "bold"),
                                  bg="#8bc34a", fg="white")
        self.discount_lbl.place(x=124, y=5, width=120, height=70)
        self.net_pay_lbl = Label(bill_menu_frame, text="Net Pay\n[0]", font=("gaudy old style", 12, "bold"),
                                 bg="#3f51b5", fg="white")
        self.net_pay_lbl.place(x=246, y=5, width=160, height=70)

        print_btn = Button(bill_menu_frame, text="Print",command=self.print_bill,cursor="hand2", font=("gaudy old style", 12, "bold"),
                           bg="lightGreen", fg="white")
        print_btn.place(x=2, y=80, width=120, height=50)
        clear_btn = Button(bill_menu_frame, text="Clear All", cursor="hand2",command=self.clear_all, font=("gaudy old style", 12, "bold"),
                           bg="grey", fg="white")
        clear_btn.place(x=124, y=80, width=120, height=50)
        generate_btn = Button(bill_menu_frame, text="Generate/Save Bill", command=self.generate_bill,
                              cursor="hand2", font=("gaudy old style", 12, "bold"), bg="#009688",
                              fg="white")
        generate_btn.place(x=246, y=80, width=160, height=50)

        # =============================[ Footer ]====================================================================
        line = Label(self.root, padx=20, relief=RAISED, bg="lightGray", fg="white")
        line.place(x=0, y=670, relwidth=1.0, height=30)

        W_line = Label(self.root, padx=20, bg="white", fg="white")
        W_line.place(x=0, y=700, relwidth=1.0, height=30)

        footer = Label(self.root, text="IMS | Inventory management system \n for any technical issue contact us: "
                                       "+91 76XXXXXXXX", font=("times new roman", 10), padx=20, bg="gray", fg="white")
        footer.place(x=0, y=730, relwidth=1.0, height=60)
        self.show()
        self.time_date()
        # self.bill_update()

        # ===============================[ Function ]===================================================================

    # num= button data
    def get_input(self, num):
        x_num = self.varCal_in.get() + str(num)
        self.varCal_in.set(x_num)

    def clear(self):
        self.varCal_in.set("")

    def perform(self):
        result = self.varCal_in.get()
        self.varCal_in.set(eval(result))

    def show(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            cur.execute("SELECT pid,Name,Price,QTY ,status FROM Product WHERE status='Active' ")
            rows = cur.fetchall()
            self.pro_table.delete(*self.pro_table.get_children())
            for i in rows:
                self.pro_table.insert('', END, values=i)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def search(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Select a valid search criteria", parent=self.root)
            else:
                cur.execute("SELECT pid,Name,Price,QTY,Status FROM Product WHERE Name LIKE %s AND status='Active' ",
                            ('%' + self.var_search.get() + '%',))

                rows = cur.fetchall()
                if len(rows) != 0:
                    self.pro_table.delete(*self.pro_table.get_children())
                    for row in rows:
                        self.pro_table.insert('', END, values=row)
                else:
                    messagebox.showinfo("Info", "No Records Found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def get_data(self,ev):
        select_row = self.pro_table.focus()
        data = self.pro_table.item(select_row)
        row = data['values']
        self.var_pid.set(row[0]),
        self.var_pro_name.set(row[1]),
        self.var_price.set(row[2]),
        self.In_stock_lbl.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_data_cart(self, ev):
        select_row = self.Cart_table.focus()
        data = self.Cart_table.item(select_row)
        row = data['values']
        self.var_pid.set(row[0]),
        self.var_pro_name.set(row[1]),
        self.var_price.set(row[2]),
        self.var_qty.set(row[3]),
        self.In_stock_lbl.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])


    def add_update_cart(self):
        if self.var_pid.get() == "":
            messagebox.showerror('Error', "Please select product from the list", parent=self.root)

        elif self.var_qty.get() == "":
            messagebox.showerror('Error', "Quantity is required", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error',"Invalid Quantity", parent=self.root)

        else:
            # price_cal = float(int(self.var_qty.get()) * float(self.var_price.get()))
            # print(price_cal)
            price_cal = self.var_price.get()
            cart_data = [self.var_pid.get(), self.var_pro_name.get(), price_cal, self.var_qty.get(),self.var_stock.get()]
            # print(self.cart_list)
            # ===========update cart===========
            present = 'no'
            index = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirm', "product is already present do you want to update "
                                                    "| remove from the cart list ", parent=self.root)
                if op == True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index)
                    else:
                        # self.cart_list[index][2] = price_cal
                        self.cart_list[index][3] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()



    def show_cart(self):
        try:
            self.Cart_table.delete(*self.Cart_table.get_children())
            for i in self.cart_list:
                self.Cart_table.insert('', END, values=i)
        except Exception as ex:
            messagebox.showerror('Error', f"Error due to : {str(ex)}", parent=self.root)

    def bill_update(self):
        self.bill_amt = 0


        for row in self.cart_list:
            self.bill_amt = self.bill_amt + (float(row[2])*int(row[3]))

            self.discount = (self.bill_amt * 5) / 100
            self.net_pay = float(self.bill_amt - self.discount)
            self.amount_lbl.config(text=f"Bill Amount(Rs.)\n[{str(self.bill_amt)}]")
            self.net_pay_lbl.config(text=f"Net Pay(Rs.)\n[{str(self.net_pay)}]")
            self.discount_lbl.config(text=f"Discount\n[{str(self.discount)}]")


    def generate_bill(self):
        if self.var_cust_name.get() == '' or self.var_contact.get() == '':
            messagebox.showerror('Error',f"Customer details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror('Error',f" Please Add Product to the Cart",parent=self.root)


        else:
#             =====Bill Top=========
            self.bill_top()
#             =====Bill Middle======
            self.bill_middle()
#             =====Bill Bottom======
            self.bill_bottom()

            fp = open(f'Bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('saved',"Bill Has been generated/Save in backend",parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 784385734, Delhi-

{str("_"*47)}
Customer Name: {self.var_cust_name.get()}
Ph no.:{self.var_contact.get()}
Bill No.{str(self.invoice)}\t\tDate:{str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
Product Name\t\t\tQty\tPrice
{str("_"*47)}\n
    
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_middle(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                qty = int(row[4]) - int(row[3])

                # Update status based on quantity comparison
                if qty == 0:
                    status = 'Inactive'
                else:
                    status = 'Active'

                price = float(row[2]) * int(row[3])
                price = str(price)

                self.txt_bill_area.insert(END, "\n " + name + "\t\t\t" + row[3] + "\tRs." + price)
                # Update qty in product table
                cur.execute("UPDATE Product SET qty=%s, status=%s WHERE pid=%s", (qty, status, pid))
                con.commit()
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def clear_cart(self):
        self.var_pid.set(''),
        self.var_pro_name.set(''),
        self.var_price.set(''),
        self.In_stock_lbl.config(text=f"In Stock")
        self.var_stock.set('')
        self.var_qty.set('')
    def clear_all(self):
        del self.cart_list[:]
        self.var_cust_name.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
    def time_date(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.clock.config(text=f"Welcome to Inventory\t\t Date:{date_}\t\t Time:{time_}")
        self.clock.after(200, self.time_date)
    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'Print')
        else:
            messagebox.showerror('Print',"Please generate bill, to print the receipt",parent=self.root)




    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("_"*47)}
Bill Amount\t\t\tRs.{self.bill_amt}
Discount\t\t\tRs.{self.discount}
Net Pay\t\t\tRs.{self.net_pay}
{str("_"*47)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)




if __name__ == "__main__":
    root = Tk()
    obj = Bill_class(root)

    root.mainloop()
