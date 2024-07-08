from tkinter import *
from tkinter import ttk, messagebox
import os

class Salesclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1526x605+0+127")
        self.root.title("Product ")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_qty = StringVar()

        title = Label(self.root, compound="left", text="View Customer Bill",
                      font=("times new roman", 30, "bold"), padx=20, bg="#000c69", fg="white", relief=RIDGE)
        title.place(x=10, y=20, width=1500, height=60)

        # Search = Label(self.root, text="Invoice No.", font=("gaudy old style", 12, "bold"), bg="lightGrey")
        # Search.place(x=50, y=100)

        # qty = Entry(self.root, textvariable=self.var_qty, bg="lightYellow", font=("times new roman", 15))
        # qty.place(x=150, y=100, width=150)

        # b1 = Button(self.root, text="Search", cursor="hand2", font=("arial", 15, "bold"), bg="yellow", command=self.search_invoice)
        # b1.place(x=315, y=100, width=150, height=28)
        #
        # b2 = Button(self.root, text="Clear", cursor="hand2", font=("arial", 15, "bold"), bg="green", command=self.clear_fields)
        # b2.place(x=475, y=100, width=150, height=28)

        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=200, height=330)
        scroll_y = Scrollbar(sales_Frame, orient=VERTICAL)

        self.sales_listbox = Listbox(sales_Frame, font=("gaudy old style", 15, "bold"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.sales_listbox.yview)

        self.sales_listbox.pack(fill=BOTH, expand=1)
        self.populate_sales_listbox()

        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=140, width=600, height=330)
        scroll_y2 = Scrollbar(bill_frame, orient=VERTICAL)

        self.bill_text_area = Text(bill_frame, font=("gaudy old style", 15, "bold"), bg="lightyellow", yscrollcommand=scroll_y2.set)
        scroll_y2.pack(side=RIGHT, fill=Y)
        scroll_y2.config(command=self.bill_text_area.yview)

        self.bill_text_area.pack(fill=BOTH, expand=1)

        bill_lbl = Label(bill_frame, text=" Customer Bill Area.", font=("gaudy old style", 12, "bold"))
        bill_lbl.pack()

        self.sales_listbox.bind('<<ListboxSelect>>', self.open_selected_file)

    def search_invoice(self):
        # Add code for searching invoice
        pass

    def clear_fields(self):
        # Add code for clearing fields
        pass

    def populate_sales_listbox(self):
        # Directory containing .txt files
        directory = '/path/to/your/directory'  # Change this to the directory path containing your .txt files

        # Traverse the directory and insert .txt files into the Listbox
        for filename in os.listdir("Bill"):
            if filename.endswith('.txt'):
                self.sales_listbox.insert(END, filename)

    def open_selected_file(self, event):
        selected_index = self.sales_listbox.curselection()
        if selected_index:
            # Get the text of the selected item (file name)
            filename = self.sales_listbox.get(selected_index)
            directory = ''  # Change this to the directory path containing your .txt files

            # Read the content of the selected file
            file_path = os.path.join("Bill", filename)
            with open(file_path, 'r') as file:
                content = file.read()
                self.bill_text_area.delete(1.0, END)
                self.bill_text_area.insert(END, content)

if __name__ == "__main__":
    root = Tk()
    obj = Salesclass(root)
    root.mainloop()
