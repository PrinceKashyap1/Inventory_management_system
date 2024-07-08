from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as mysql


class Productclass:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1220x610+305+135")
        self.root.geometry("1526x605+0+127")
        self.root.title("Product ")
        self.root.config(bg="white")
        self.root.focus_force()
        # ==============================================================================================================

        # =============================[ Variable ]=====================================================================
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()
        self.var_cat = StringVar()
        self.var_supp = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.root['bg'] = "lightGrey"
        # =============================[ Frame ]=======================================================================

        pro_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        pro_frame.place(x=65, y=10, width=450, height=550)
        pro_frame['bg'] = "#c4c3d0"

        #         title
        pro_title = Label(pro_frame, font=("times new roman", 19), text="Product Details", bg="#0e3b84", fg="white")
        pro_title.pack(side=TOP, fill=X)

        pro_cat = Label(pro_frame, text="Category", bg="#c4c3d0", font=("times new roman", 15))
        pro_cat.place(x=30, y=60)

        supp = Label(pro_frame, text="Supplier", bg="#c4c3d0", font=("times new roman", 15))
        supp.place(x=30, y=120)

        name = Label(pro_frame, text="Name", bg="#c4c3d0", font=("times new roman", 15))
        name.place(x=30, y=180)

        pro_name = Label(pro_frame, text="Product Name", bg="#c4c3d0", font=("times new roman", 15))
        pro_name.place(x=30, y=180)

        price = Label(pro_frame, text="Price", bg="#c4c3d0", font=("times new roman", 15))
        price.place(x=30, y=240)

        qty = Label(pro_frame, text="QTY", bg="#c4c3d0", font=("times new roman", 15))
        qty.place(x=30, y=300)

        status = Label(pro_frame, text="Status", bg="#c4c3d0", font=("times new roman", 15))
        status.place(x=30, y=360)

        # =============================[ Combobox OF Category and Supplier ]============================================

        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        cur.execute("SELECT Name FROM Category")
        opt_cat = cur.fetchall()

        self.var_cat.set("Select")

        cmb_search = ttk.Combobox(pro_frame, textvariable=self.var_cat, values=opt_cat,
                                  state="readonly", justify="center",
                                  font=("gaudy old style", 15))
        cmb_search.place(x=150, y=60, width=180)
        # cmb_search.current(0)

        cur.execute("SELECT Name FROM Supplier")
        opt_supp = cur.fetchall()
        cmb_search = ttk.Combobox(pro_frame, textvariable=self.var_supp, values=opt_supp, state="readonly",
                                  justify="center", font=("gaudy old style", 15))
        cmb_search.place(x=150, y=120, width=180)

        self.var_supp.set("Select")
        # cmb_search.current(0)

        pro_name_txt = Entry(pro_frame, textvariable=self.var_name, bg="lightYellow", font=("times new roman", 15))
        pro_name_txt.place(x=150, y=180, width=180)

        price_txt = Entry(pro_frame, textvariable=self.var_price, bg="lightYellow", font=("times new roman", 15))
        price_txt.place(x=150, y=240, width=180)

        qty = Entry(pro_frame, textvariable=self.var_qty, bg="lightYellow", font=("times new roman", 15))
        qty.place(x=150, y=300, width=180)

        status = Entry(pro_frame, textvariable=self.var_status, bg="lightYellow", font=("times new roman", 15))
        status.place(x=150, y=360, width=180)

        # =============================[ Button ]=======================================================================

        button_save = Button(pro_frame, text="Save", command=self.add, font=("gaudy old style", 15), bg="blue",
                             cursor="hand2")
        button_save.place(x=30, y=450, width=90, height=30)
        button_Update = Button(pro_frame, text="Update", command=self.update, font=("gaudy old style", 15), bg="green",
                               cursor="hand2")

        button_Update.place(x=130, y=450, width=90, height=30)
        button_Delete = Button(pro_frame, text="Delete", command=self.delete, font=("gaudy old style", 15), bg="red",
                               cursor="hand2")
        button_Delete.place(x=230, y=450, width=90, height=30)
        button_Clear = Button(pro_frame, text="Clear", command=self.clear, font=("gaudy old style", 15), bg="gray",
                              cursor="hand2")
        button_Clear.place(x=330, y=450, width=90, height=30)

        # =============================[ Search Frame ]=================================================================

        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="lightGrey",
                                 font=("gaudy old style", 12, "bold"),
                                 bd=2, relief=RIDGE)
        SearchFrame.place(x=600, y=10, height=70, width=800)

        # =============================[ Combobox of Search ]===========================================================

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_search_by,
                                  values=("search", "Category", "Supplier", "Name"), state="readonly", justify="center",
                                  font=("gaudy old style", 15))
        cmb_search.place(x=30, y=10, width=220)
        cmb_search.current(0)

        text_search = Entry(SearchFrame, textvariable=self.var_search_text, font=("gaudy old style", 15),
                            bg="light yellow")
        text_search.place(x=265, y=10,width=300)

        button_search = Button(SearchFrame, text="Search",command=self.search, font=("gaudy old style", 15),
                               bg="green", cursor="hand2")
        button_search.place(x=580, y=9, width="200", height="30")

        # =============================[ Product Details ]==============================================================

        pro_frame = Frame(self.root, bd=3, bg="lightGrey", relief=RIDGE)
        pro_frame.place(x=600, y=90, height=470, width=800)

        scroll_x = Scrollbar(pro_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(pro_frame, orient=VERTICAL)

        self.pro_detail = ttk.Treeview(pro_frame, columns=(
            "pid", "Supplier", "Category", "Name", "price", "qty", "status"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.pro_detail.bind("<ButtonRelease-1>", self.get_data)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.pro_detail.xview)
        scroll_y.config(command=self.pro_detail.yview)
        # =============================[ Heading ]======================================================================

        self.pro_detail.heading("pid", text="Product Id")
        self.pro_detail.heading("Supplier", text="Supplier")
        self.pro_detail.heading("Category", text="Category")
        self.pro_detail.heading("Name", text="Name")
        self.pro_detail.heading("price", text="Price")
        self.pro_detail.heading("qty", text="QTY")
        self.pro_detail.heading("status", text="Status")
        self.pro_detail["show"] = "headings"

        self.pro_detail.column("pid", width=80)
        self.pro_detail.column("Supplier", width=80)
        self.pro_detail.column("Category", width=80)
        self.pro_detail.column("Name", width=80)
        self.pro_detail.column("price", width=80)
        self.pro_detail.column("qty", width=80)
        self.pro_detail.column("status", width=80)
        self.pro_detail.pack(fill=BOTH, expand=1)
        self.show()




    # =============================[ Function ]=========================================================================

    def search(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:
            if self.var_search_by.get() == "search":
                messagebox.showerror("Error", "Select a valid search criteria", parent=self.root)
            elif self.var_search_by.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)

            else:
                cur.execute("SELECT * FROM Product WHERE " + self.var_search_by.get() + " LIKE %s",
                            ("%" + self.var_search_text.get() + "%",))

                rows = cur.fetchall()
                if len(rows) != 0:
                    self.pro_detail.delete(*self.pro_detail.get_children())
                    for row in rows:
                        self.pro_detail.insert('', END, values=row)
                else:
                    messagebox.showinfo("Info", "No Records Found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def add(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:

            if self.var_cat.get() == "Select" or self.var_supp.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "All field Must Be Required", parent=self.root)


            else:
                cur.execute("SELECT * FROM Product WHERE Name = %s", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", " already assigned, try different", parent=self.root)
                else:

                    cur.execute(
                        "INSERT INTO Product (Category, Supplier, Name, price, qty, status) VALUES(%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_cat.get(),
                            self.var_supp.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get()

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Product details added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def get_data(self, ev):
        select_row = self.pro_detail.focus()
        data = self.pro_detail.item(select_row)

        self.var_supp.set(data['values'][1]),
        self.var_cat.set(data['values'][2]),
        self.var_name.set(data['values'][3]),
        self.var_price.set(data['values'][4]),
        self.var_qty.set(data['values'][5]),
        self.var_status.set(data['values'][6]),

    def show(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Product")
            rows = cur.fetchall()
            self.pro_detail.delete(*self.pro_detail.get_children())
            for i in rows:
                self.pro_detail.insert('', END, values=i)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def update(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:

            if self.var_cat.get() == "Select":
                messagebox.showerror("Error", "Please select the Category", parent=self.root)
            elif self.var_supp.get() == "Select":
                messagebox.showerror("Error", "Please select the Supplier", parent=self.root)
            elif self.var_name.get() == "":
                messagebox.showerror("Error", "Please enter the Name", parent=self.root)

            else:
                cur.execute("SELECT * FROM Product WHERE Name = %s", (self.var_name.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Product is not in table", parent=self.root)
                else:

                    cur.execute("UPDATE Product SET  Category = %s,Supplier = %s,price = %s,qty = %s,status = %s"
                                " WHERE Name= %s ",
                                (
                                    self.var_cat.get(),
                                    self.var_supp.get(),

                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                                    self.var_name.get()

                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def delete(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:

            if self.var_name.get() == "":
                messagebox.showerror("Error", " Please Select Or Enter to delete", parent=self.root)
            else:
                cur.execute("SELECT * FROM Product WHERE Name = %s", (self.var_name.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Product is not in table", parent=self.root)
                else:
                    ok = messagebox.askyesno("Confirm", "do you want to delete?", parent=self.root)
                    if ok:
                        cur.execute("DELETE FROM Product WHERE Name = %s", (self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Product Deleted successfully", parent=self.root)
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def clear(self):
        # clear all the variables
        self.var_cat.set("Select"),
        self.var_supp.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set(""),

        self.pro_detail.selection_remove(self.pro_detail.selection())


if __name__ == "__main__":
    root = Tk()
    obj = Productclass(root)
    root.mainloop()
