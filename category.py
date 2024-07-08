from tkinter import *
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
import mysql.connector as mysql


class Categoryclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1526x605+0+127")
        self.root.title("Category ")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root['bg'] = "lightGrey"

        # =========================[ variable  ]========================================================================
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        # ==============================[ title ]=======================================================================

        cat_title = Label(self.root, font=("times new roman", 30, "bold"), bd=3, relief=RIDGE,
                          text="Manage Product Category", bg="#0e3b84", fg="white")
        cat_title.pack(side=TOP, fill=X, padx=10, pady=20)


        cat_name = Label(self.root, text="Enter Category Name", font=("times new roman", 30, "bold"), bg="lightGrey",
                         fg="black")
        cat_name.place(x=50, y=100)


        cat_txt = Entry(self.root, textvariable=self.var_name, font=("times new roman", 18, "bold"), bg="lightYellow",
                        fg="black")
        cat_txt.place(x=50, y=170, width=300)

        # =====================================[ Button ]===============================================================

        cat_add = Button(self.root, text="Add", command=self.add, font=("times new roman", 15, "bold"), bg="#4caf50",
                         fg="black", cursor="hand2")
        cat_add.place(x=360, y=170, width=150, height=30)


        cat_delete = Button(self.root, text="Delete", command=self.delete, font=("times new roman", 15, "bold"),
                            bg="red", fg="black", cursor="hand2")
        cat_delete.place(x=520, y=170, width=150, height=30)

        # ===========================[ Product details ]================================================================

        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=1200, y=100, width=300, height=425)

        scroll_x = Scrollbar(cat_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(cat_frame, orient=VERTICAL)

        self.cat_table = ttk.Treeview(cat_frame, columns=("Cid", "Name"), yscrollcommand=scroll_y.set,
                                      xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cat_table.xview)
        scroll_x.config(command=self.cat_table.yview)
        self.cat_table.heading("Cid", text=" C id")
        self.cat_table.heading("Name", text=" Name")

        self.cat_table["show"] = "headings"

        self.cat_table.column("Cid", width=90)
        self.cat_table.column("Name", width=90)

        self.cat_table.pack(fill=BOTH, expand=1)
        self.cat_table.bind("<ButtonRelease-1>", self.get_data)

        self.image1 = Image.open("image/img_1.png")
        self.image1 = self.image1.resize((560, 300))
        self.image1 = ImageTk.PhotoImage(self.image1)

        self.img1_lbl = Label(self.root, image=self.image1, relief=RAISED)
        self.img1_lbl.place(x=50, y=220)

        self.image2 = Image.open("image/img_2.png")
        self.image2 = self.image2.resize((560, 300))
        self.image2 = ImageTk.PhotoImage(self.image2)

        self.img2_lbl = Label(self.root, image=self.image2, relief=RAISED)
        self.img2_lbl.place(x=620, y=220)
        self.show()

    # ================================[ function ]======================================================================

    def show(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Category")
            rows = cur.fetchall()
            self.cat_table.delete(*self.cat_table.get_children())
            for i in rows:
                self.cat_table.insert('', END, values=i)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

    def get_data(self, ev):
        select_row = self.cat_table.focus()
        data = self.cat_table.item(select_row)

        self.var_cat_id.set(data['values'][0]),
        self.var_name.set(data['values'][1]),

    def add(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()

        try:

            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name should be required ", parent=self.root)
            else:
                cur.execute("SELECT * FROM Category WHERE Name = %s", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This  category already present try different", parent=self.root)
                else:

                    cur.execute(
                        "INSERT INTO Category (Name) VALUES(%s)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()
                    self.var_cat_id.set("")
                    self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()

    def delete(self):
        con = mysql.connect(host="localhost", user="root", password="prince@123", database="new_schema")
        cur = con.cursor()
        try:
            Id = self.var_cat_id.get()
            if Id == "":
                messagebox.showerror("Error", "Please select Category from the list", parent=self.root)
            else:
                cur.execute("SELECT * FROM Category WHERE Cid = %s", (Id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Error, Please try again", parent=self.root)
                else:
                    ok = messagebox.askyesno("Confirm", "do you want to delete?", parent=self.root)
                    if ok:
                        cur.execute("DELETE FROM Category WHERE Cid = %s", (Id,))
                        con.commit()
                        messagebox.showinfo("Success", "Employee Deleted successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)

        finally:
            if con:
                con.close()


if __name__ == "__main__":
    root = Tk()
    obj = Categoryclass(root)
    root.mainloop()
