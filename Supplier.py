from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as mysql


class Supplierclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1526x605+0+127")
        self.root.title("Supplier ")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root['bg'] ="lightgrey"
        # ===================================
        # ===========all variable============

        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()

        self.var_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()





        #         ==========Title===============================
        supp_title = Label(self.root, font=("times new roman", 20, "bold"), text="Manage Supplier Details", bg="#0e3b84", fg="white")
        supp_title.place(x=10, y=20, width=1500,)

        #         ========Content=====================

        #         ====row1====
        supplier_invoice = Label(self.root, font=("goudy old style", 15), text="Invoice no.", bg="lightgrey").place(x=10, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_invoice, font=("gaudy old style", 15),
                                     bg="light yellow").place(x=120, y=80, width=180)
        #   ====row2====
        supp_name = Label(self.root, font=("goudy old style", 15), text="Supplier Name", bg="lightgrey").place(x=10, y=130)

        txt_supp_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),
                             bg="light yellow").place(x=140, y=130, width=180)
        #   ====row3====
        contact = Label(self.root, font=("goudy old style", 15), text="Contact", bg="lightgrey").place(x=10, y=180)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15),
                            bg="light yellow").place(x=120, y=180, width=180)
        #   ====row4====
        descrip = Label(self.root, font=("goudy old style", 15), text="Description", bg="lightgrey").place(x=10, y=230)
        self.txt_descrip = Text(self.root,wrap=WORD, font=("goudy old style", 15),bg="light yellow")
        self.txt_descrip.place(x=120, y=230, width=600,height=180)

        #         ======               >>>>>>>>>Button<<<<<<<<              =========

        button_save = Button(self.root, text="Save",command=self.add, font=("goudy old style", 15), bg="#f93737",
                             cursor="hand2").place(x=120, y=480, width=120, height=40)
        button_Update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 15), bg="#dee100",
                               cursor="hand2").place(x=250, y=480, width=120, height=40)
        button_Delete = Button(self.root, text="Delete",command=self.delete,  font=("goudy old style", 15), bg="#71a438",
                               cursor="hand2").place(x=380, y=480, width=120, height=40)
        button_Clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#333cf4",
                              cursor="hand2").place(x=510, y=480, width=120, height=40)

        #         ==========invoice no ==========
        invoice = Label(self.root, font=("goudy old style", 15), text="Invoice ", bg="lightgrey")
        invoice.place(x=730, y=100, width=180)

        txt_invoice = Entry(self.root, textvariable=self.var_searchtext, font=("goudy old style", 15),
                            bg="light yellow").place(x=870, y=100, width=370)

        button_search = Button(self.root, text="Search", command=self.search,font=("gaudy old style", 15),
                               bg="green", cursor="hand2")
        button_search.place(x=1250, y=100, width="130", height="30")

        # =============Supplier details============
        supp_frame = Frame(self.root, bd=3, bg="white",relief=RIDGE)
        supp_frame.place(x=780, y=150,width=600, height=370 )

        scrollx = Scrollbar(supp_frame,orient=HORIZONTAL)
        scrolly = Scrollbar(supp_frame,orient=VERTICAL)

        self.supp_table = ttk.Treeview(supp_frame,columns=("Invoice","Name","Contact", "Description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.supp_table.bind("<ButtonRelease-1>", self.get_data)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supp_table.xview)
        scrolly.config(command=self.supp_table.yview)
#         =========heading========

        self.supp_table.heading("Invoice", text="Invoice")
        self.supp_table.heading("Name", text="Name")
        self.supp_table.heading("Contact", text="Contact")
        self.supp_table.heading("Description", text="Description")
        self.supp_table["show"] = "headings"

        self.supp_table.column("Invoice", width=90)
        self.supp_table.column("Name", width=90)
        self.supp_table.column("Contact", width=90)
        self.supp_table.column("Description", width=90)
        self.supp_table.pack(fill=BOTH,expand=1)

        self.show()

#         function
#
    def search(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
    #
    #
        try:
            if self.var_searchby.get() == " ":
                messagebox.showerror("ERROR", "Please Enter Invoice number")
            else:


                search_txt = '%' + self.var_searchtext.get() + '%'


                cur.execute("SELECT * FROM Supplier WHERE Invoice LIKE %s", (search_txt,))
                rows = cur.fetchall()
    #
    #             # check the row is existed or not
                if rows == 0:
                    messagebox.showinfo("Info", "No Record Found ", parent=self.root)
                else:
                    self.supp_table.delete(*self.supp_table.get_children())
                    for row in rows:
                        self.supp_table.insert('', END, values=row)




        except Exception as ex:
            messagebox.showerror("Error", f"Error due to{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()


    def get_data(self, ev):
        select_row = self.supp_table.focus()
        data = self.supp_table.item(select_row)

        self.var_invoice.set(data['values'][0]),
        self.var_name.set(data['values'][1]),

        self.var_contact.set(data['values'][2]),

        self.txt_descrip.delete("1.0",END)

        self.txt_descrip.insert(END,data['values'][3])

    def add(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:

            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Supplier Invoice Must Be Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Supplier WHERE Invoice = %s", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Supplier already assigned, try different", parent=self.root)
                else:

                    cur.execute(
                        "INSERT INTO Supplier (Invoice ,Name,Contact,Description) VALUES(%s,%s,%s,%s)",
                        (
                            self.var_invoice.get(),
                            self.var_name.get(),

                            self.var_contact.get(),

                            self.txt_descrip.get('1.0',END)


                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def update(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:

            if self.var_invoice.get() == "":
                messagebox.showerror("Error", "Supplier ID Must Be Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Supplier WHERE Invoice = %s", (self.var_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Supplier Invoice is not in table", parent=self.root)
                else:

                    cur.execute("UPDATE Supplier SET  Name = %s,Contact = %s,Description = %s WHERE Invoice = %s",

                                (

                                    self.var_name.get(),

                                    self.var_contact.get(),


                                    self.txt_descrip.get('1.0',END),
                                    self.var_invoice.get()


                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()


    def show(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Supplier")
            rows = cur.fetchall()
            self.supp_table.delete(*self.supp_table.get_children())
            for i in rows:
                self.supp_table.insert('', END, values=i)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)


    def delete(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            Id = self.var_invoice.get()
            if Id == "":
                messagebox.showerror("Error", "Supplier Invoice Must Be Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Supplier WHERE Invoice = %s", (Id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Supplier Invoice is not in table", parent=self.root)
                else:
                    ok = messagebox.askyesno("Confirm", "do you want to delete?", parent=self.root)
                    if ok:
                        cur.execute("DELETE FROM Supplier WHERE Invoice = %s", (Id,))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier Deleted successfully", parent=self.root)
                        # self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def clear(self):
        # clear all the variables
        self.var_invoice.set(""),
        self.var_name.set(""),

        self.var_contact.set(""),

        self.txt_descrip.delete('1.0',END),



        self.supp_table.selection_remove(self.supp_table.selection())

    







if __name__ == "__main__":
    root = Tk()
    obj = Supplierclass(root)
    root.mainloop()
