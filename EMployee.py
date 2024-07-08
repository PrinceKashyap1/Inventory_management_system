from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql


class Employeclass:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1526x605+0+127")
        self.root.title("Employee ")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root['bg'] = "lightGrey"

        # ==============================================================================================================

        # ==============================================[ all variable ]================================================

        self.var_search_by = StringVar()
        self.var_search_text = StringVar()

        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_password = StringVar()
        self.var_usertype = StringVar()
        self.Emp_address = StringVar()
        self.var_salary = StringVar()

        # ===========================================[ search frame ]===================================================

        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="lightGrey",
                                 font=("gaudy old style", 12, "bold"),
                                 bd=5, relief=RIDGE)
        SearchFrame.place(x=500, y=10, height=70, width=600)

        # ===========================================[ combo box option ]===============================================

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_search_by,
                                  values=("search", "Email", "Name", "Contact"), state="readonly", justify="center",
                                  font=("gaudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        text_search = Entry(SearchFrame, textvariable=self.var_search_text, font=("gaudy old style", 15),
                            bg="light yellow")
        text_search.place(x=200, y=10)
        # ======Search Button=====
        button_search = Button(SearchFrame, text="Search", command=self.search, font=("gaudy old style", 15),
                               bg="green", cursor="hand2")
        button_search.place(x=420, y=9, width="150", height="30")

        #         ==========Title===============================
        Emp_title = Label(self.root, font=("times new roman", 19), text="Employee Details", bg="#0e3b84", fg="white")
        Emp_title.place(x=35, y=100, width=1450)

        # ========================================[ Content ]===========================================================

        # ========================================[ row1 ]==============================================================

        Emp_Id = Label(self.root, font=("gaudy old style", 15), text="Emp. Id", bg="lightGrey")
        Emp_Id.place(x=210, y=150)
        gender = Label(self.root, font=("gaudy old style", 15), text="Gender", bg="lightGrey")
        gender.place(x=700, y=150)
        contact = Label(self.root, font=("gaudy old style", 15), text="Contact", bg="lightGrey")
        contact.place(x=1100, y=150)

        txt_Emp_Id = Entry(self.root, textvariable=self.var_emp_id, font=("gaudy old style", 15), bg="light yellow")
        txt_Emp_Id.place(x=320, y=150, width=180)

        # =====================================[ ComboBox OF Gender ]===================================================

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"),
                                  state="readonly", justify="center", font=("gaudy old style", 15))
        cmb_gender.place(x=800, y=150, width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("gaudy old style", 15), bg="light yellow")
        txt_contact.place(x=1200, y=150, width=180)

        # ========================================[ row2 ]==============================================================

        Emp_name = Label(self.root, font=("gaudy old style", 15), text="Name", bg="lightGrey")
        Emp_name.place(x=210, y=200)
        Emp_dob = Label(self.root, font=("gaudy old style", 15), text="D.O.B", bg="lightGrey")
        Emp_dob.place(x=700, y=200)
        Emp_doj = Label(self.root, font=("gaudy old style", 15), text="D.O.J", bg="lightGrey")
        Emp_doj.place(x=1100, y=200)

        txt_Emp_name = Entry(self.root, textvariable=self.var_name, font=("gaudy old style", 15), bg="light yellow")
        txt_Emp_name.place(x=320, y=200, width=180)
        txt_Emp_dob = Entry(self.root, textvariable=self.var_dob, font=("gaudy old style", 15), bg="light yellow")
        txt_Emp_dob.place(x=800, y=200, width=180)
        txt_Emp_doj = Entry(self.root, textvariable=self.var_doj, font=("gaudy old style", 15), bg="light yellow")
        txt_Emp_doj.place(x=1200, y=200, width=180)

        # ========================================[ row3 ]==============================================================

        Emp_email = Label(self.root, font=("gaudy old style", 15), text="Email", bg="lightGrey")
        Emp_email.place(x=210, y=250)


        Emp_password = Label(self.root, font=("gaudy old style", 15), text="Password", bg="lightGrey")
        Emp_password.place(x=700, y=250)

        Emp_usertype = Label(self.root, font=("gaudy old style", 15), text="Usertype", bg="lightGrey")
        Emp_usertype.place(x=1100, y=250)

        txt_Emp_email = Entry(self.root, textvariable=self.var_email, font=("gaudy old style", 15), bg="light yellow")
        txt_Emp_email.place(x=320, y=250, width=180)

        txt_Emp_password = Entry(self.root, textvariable=self.var_password, font=("gaudy old style", 15),
                                 bg="light yellow")
        txt_Emp_password.place(x=800, y=250, width=180)

        # ============================[ ComboBox Of UserType ]==========================================================

        cmb_usertype = ttk.Combobox(self.root, textvariable=self.var_usertype, values=("Admin", "Employee"),
                                    state="readonly", justify="center", font=("gaudy old style", 15))
        cmb_usertype.place(x=1200, y=250, width=180)
        cmb_usertype.current(0)

        # ============================[ Row 4 ]=========================================================================

        Emp_address = Label(self.root, font=("gaudy old style", 15), text="Address", bg="lightGrey")
        Emp_address.place(x=210, y=300)

        Emp_salary = Label(self.root, font=("gaudy old style", 15), text="Salary", bg="lightGrey")
        Emp_salary.place(x=700, y=300)

        self.txt_Emp_address = Entry(self.root, textvariable=self.Emp_address, font=("gaudy old style", 15),
                                     bg="light yellow")
        self.txt_Emp_address.place(x=320, y=300, width=270, height=70)

        txt_Emp_salary = Entry(self.root, textvariable=self.var_salary, font=("gaudy old style", 15), bg="light yellow")
        txt_Emp_salary.place(x=800, y=300, width=180)

        # =============================[ Button ]=======================================================================

        button_save = Button(self.root, text="Save", command=self.add, font=("gaudy old style", 15), bg="#f93737",
                             cursor="hand2")
        button_save.place(x=700, y=340, width=110, height=30)
        button_Update = Button(self.root, text="Update", command=self.update, font=("gaudy old style", 15),
                               bg="#dee100", cursor="hand2")
        button_Update.place(x=820, y=340, width=110, height=30)
        button_Delete = Button(self.root, text="Delete", command=self.delete, font=("gaudy old style", 15),
                               bg="#71a438", cursor="hand2")
        button_Delete.place(x=940, y=340, width=110, height=30)
        button_Clear = Button(self.root, text="Clear", command=self.clear, font=("gaudy old style", 15), bg="#333cf4",
                              cursor="hand2")
        button_Clear.place(x=1060, y=340, width=110, height=30)

        # ==============================================================================================================

        # ============================[ Employee Details ]==============================================================

        Emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        Emp_frame.place(x=0, y=390, relwidth=1, height=220)

        scroll_x = Scrollbar(Emp_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Emp_frame, orient=VERTICAL)

        self.Emp_table = ttk.Treeview(Emp_frame, columns=(
            "Eid", "Name", "Email", "Gender", "Contact", "D.O.B", "D.O.J", "Pass", "usertype", "Address", "Salary"),
                                      yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.Emp_table.bind("<ButtonRelease-1>", self.get_data)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Emp_table.xview)
        scroll_y.config(command=self.Emp_table.yview)
        self.Emp_table.heading("Eid", text=" Emp Id")
        self.Emp_table.heading("Name", text=" Name")
        self.Emp_table.heading("Email", text=" Email")
        self.Emp_table.heading("Gender", text=" Gender")
        self.Emp_table.heading("Contact", text=" Contact")
        self.Emp_table.heading("D.O.B", text=" D.O.B")
        self.Emp_table.heading("D.O.J", text=" D.O.J")
        self.Emp_table.heading("Pass", text=" Password")
        self.Emp_table.heading("usertype", text="usertype")
        self.Emp_table.heading("Address", text=" Address")
        self.Emp_table.heading("Salary", text=" Salary")
        self.Emp_table["show"] = "headings"

        self.Emp_table.column("Eid", width=90)
        self.Emp_table.column("Name", width=90)
        self.Emp_table.column("Email", width=90)
        self.Emp_table.column("Gender", width=90)
        self.Emp_table.column("Contact", width=90)
        self.Emp_table.column("D.O.B", width=90)
        self.Emp_table.column("D.O.J", width=90)
        self.Emp_table.column("Pass", width=90)
        self.Emp_table.column("usertype", width=90)
        self.Emp_table.column("Address", width=90)
        self.Emp_table.column("Salary", width=90)
        self.Emp_table.pack(fill=BOTH, expand=1)
        self.show()

    # ===========================[ Frame ]==============================================================================
        # employee logo image
        self.emp_img = Image.open("image/img.png")
        self.emp_img = self.emp_img.resize((400, 350))
        self.emp_img = ImageTk.PhotoImage(self.emp_img)






    # ==================================================================================================================

    # ============================[ Function ]==========================================================================

    def search(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:
            if self.var_search_by.get() == "search":
                messagebox.showerror("Error", "Select a valid search criteria", parent=self.root)
            elif self.var_search_by.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)

            else:
                cur.execute("SELECT * FROM Employee WHERE " + self.var_search_by.get() + " LIKE %s",
                    ("%" + self.var_search_text.get() + "%",))


                rows = cur.fetchall()
                if len(rows) != 0:
                    self.Emp_table.delete(*self.Emp_table.get_children())
                    for row in rows:
                        self.Emp_table.insert('', END, values=row)
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

            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must Be Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE Eid = %s", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try different",
                                         parent=self.root)
                else:

                    cur.execute(
                        "INSERT INTO Employee (Eid,Name,Email,Gender,Contact,DOB,DOJ,Pass,usertype,Address,"
                        "Salary) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_password.get(),
                            self.var_usertype.get(),
                            self.txt_Emp_address.get(),
                            self.var_salary.get()

                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=self.root)

                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def get_data(self, ev):
        select_row = self.Emp_table.focus()
        data = self.Emp_table.item(select_row)

        self.var_emp_id.set(data['values'][0]),
        self.var_name.set(data['values'][1]),
        self.var_email.set(data['values'][2]),
        self.var_gender.set(data['values'][3]),
        self.var_contact.set(data['values'][4]),
        self.var_dob.set(data['values'][5]),
        self.var_doj.set(data['values'][6]),
        self.var_password.set(data['values'][7]),
        self.var_usertype.set(data['values'][8]),
        self.Emp_address.set(data['values'][9]),
        self.var_salary.set(data['values'][10])

    def show(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Employee")
            rows = cur.fetchall()
            self.Emp_table.delete(*self.Emp_table.get_children())
            for i in rows:
                self.Emp_table.insert('', END, values=i)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def update(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:

            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must Be Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE Eid = %s", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Employee ID is not in table", parent=self.root)
                else:

                    cur.execute("UPDATE Employee SET  Name = %s,Email = %s,Gender = %s,Contact = %s,DOB = %s,"
                                "DOJ = %s,Pass = %s,usertype = %s,Address = %s,Salary = %s WHERE Eid= %s",
                                (

                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_password.get(),
                                    self.var_usertype.get(),
                                    self.txt_Emp_address.get(),
                                    self.var_salary.get(),
                                    self.var_emp_id.get()

                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
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
            Id = self.var_emp_id.get()
            if Id == "":
                messagebox.showerror("Error", "Employee ID Must Be Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE Eid = %s", (Id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Employee ID is not in table", parent=self.root)
                else:
                    ok = messagebox.askyesno("Confirm", "do you want to delete?", parent=self.root)
                    if ok:
                        cur.execute("DELETE FROM Employee WHERE Eid = %s", (Id,))
                        con.commit()
                        messagebox.showinfo("Success", "Employee Deleted successfully", parent=self.root)
                        self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()




    #

    def clear(self):
        # clear all the variables
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_password.set(""),
        self.var_usertype.set("Admin"),
        self.Emp_address.set(""),
        self.var_salary.set("")

        self.Emp_table.selection_remove(self.Emp_table.selection())


if __name__ == "__main__":
    root = Tk()
    obj = Employeclass(root)
    root.mainloop()

