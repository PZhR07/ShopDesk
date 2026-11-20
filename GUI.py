import tkinter as tk
from Database import Table_contact, Table_products, Table_invoice_customer
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from Security import Security

class Run_contact(tk.Tk):

    def __init__(self):
        super().__init__()
        self.minsize(750, 500)
        self.title("Application")
        style = ttk.Style(self)
        style.configure("Title.TLabel", font=("Segoe UI", 50, "bold"))
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure("TLabel", font=("Segoe UI", 10))

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background="#ّF3F6FA")
        style.configure("TLabel", background="#F3F6FA", foreground="#243247")
        style.configure("TLabelframe", background="#FFFFFF")
        style.configure("TLabelframe.Label", background="#FF6692", foreground="#442269", font=("Segoe UI", 11, "bold"))
        style.configure("TEntry", padding=6)
        style.configure("TButton", padding=8, background="#46637C", foreground="#F6EDFF")
        style.map("TButton", background=[("active", "#1D4ED8")])

        self.update_idletasks()
        self.base_width = self.winfo_width()
        self.base_height = self.winfo_height()
        self.bind("<Configure>", self.resize_widgets)
        
    def widget_form(self):

        LabelFrame1 = ttk.LabelFrame(self, text = "Form")
        LabelFrame1.pack(padx = 10, pady = 10, fill = "both",)

        label1 = ttk.Label(LabelFrame1, text="first name:")
        self.entry1 = ttk.Entry(LabelFrame1, validate="key", validatecommand=(self.register(Security.checker), "%P"))
        label1.grid( row = 0, column = 0, padx = 1, pady = 1, sticky="ew")
        self.entry1.grid( row = 0, column = 1, padx = 5, pady = 5, sticky="ew")

        label2 = ttk.Label(LabelFrame1, text="last name:")
        self.entry2 = ttk.Entry(LabelFrame1, validate="key", validatecommand=(self.register(Security.checker), "%P"))
        label2.grid( row = 1, column = 0, padx = 5, pady = 5, sticky="ew")
        self.entry2.grid( row = 1, column = 1, padx = 5, pady = 5, sticky="ew")

        label3 = ttk.Label(LabelFrame1, text="number:")
        self.entry3 = ttk.Entry(LabelFrame1, validate="key",validatecommand=(self.register(Security.checker_phone), "%P"))
        label3.grid( row = 2, column = 0, padx = 5, pady = 5, sticky="ew")
        self.entry3.grid( row = 2, column = 1, padx = 5, pady = 5, sticky="ew") 
    
    def widget_menu(self):
        LabelFrame2 = ttk.LabelFrame(self, text = "Menu")
        LabelFrame2.pack(padx = 10, pady = 10, fill = "both")
        button_1 = ttk.Button(LabelFrame2, text = "Append", command = self.add_contact, width = 50)
        button_2 = ttk.Button(LabelFrame2, text = "Erase", command = lambda: Table_contact.erase(self.entry3.get()), width = 50)
        button_3 = ttk.Button(LabelFrame2, text = "Modify", command = lambda: Table_contact.modify(self.entry1.get(), self.entry2.get(), self.entry3.get()), width = 50)
        button_4 = ttk.Button(LabelFrame2, text = "Find", command = self.find_contact, width = 50)
        button_5 = ttk.Button(LabelFrame2, text = "Display", command = self.display_contacts, width = 50)
        button_6 = ttk.Button(LabelFrame2, text = "Backup", command = lambda: Table_contact.backup(), width = 50)
        button_7 = ttk.Button(LabelFrame2, text = "CSV_Backup", command= lambda: Table_contact.csv_backup(), width = 50)
        button_1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="ew")
        button_2.grid(row = 1, column = 0, padx = 5, pady = 5, sticky="ew")
        button_3.grid(row = 2, column = 0, padx = 5, pady = 5, sticky="ew")
        button_4.grid(row = 3, column = 0, padx = 5, pady = 5, sticky="ew")
        button_5.grid(row = 4, column = 0, padx = 5, pady = 5, sticky="ew")
        button_6.grid(row = 5, column = 0, padx = 5, pady = 5, sticky="ew")
        button_7.grid(row = 6, column = 0, padx = 5, pady = 5, sticky="ew")
    
    def widget_print(self):
        Labelframe3 = ttk.LabelFrame(self, text="Print")
        Labelframe3.pack(padx=10, pady=10, fill="both", side = "right")

        self.output = tk.Text(Labelframe3, height=12, width=70)
        self.output.pack(fill="both", expand=True, padx=5, pady=5)

    def show_contacts(self, rows):
        self.output.delete("1.0", tk.END)
        if not rows:
            self.output.insert(tk.END, "Contact not find")
            return

        for row in rows:
            self.output.insert(tk.END, f"{row[1]} | {row[2]} | {row[3]} | {row[4]}\n")

    def find_contact(self):
        rows = Table_contact.find(self.entry2.get(),self.entry3.get())
        self.show_contacts(rows)

    def display_contacts(self):
        rows = Table_contact.display_all()
        self.show_contacts(rows)

    def add_contact(self):
        number = self.entry3.get()

        if not Security.valid_phone(number):
            messagebox.showerror("Number must be 11 letter.")
            return

        Table_contact.append(self.entry1.get(), self.entry2.get(), number)

    def resize_widgets(self, event):
        if event.widget is not self:
            return

        scale = min(event.width / self.base_width, event.height / self.base_height)

        for widget in self.winfo_children():
            self.resize_widget(widget, scale)

    def resize_widgets(self, event):
        if event.widget is not self:
            return

        scale_x = event.width / self.base_width
        scale_y = event.height / self.base_height
        scale = min(scale_x, scale_y)

        font_size = max(8, int(10 * scale))
        entry_width = max(10, int(20 * scale))
        button_width = max(10, int(15 * scale))
        
class Run_product(tk.Tk):

    def __init__(self):
        super().__init__()
        self.minsize(750, 500)
        self.title("Application")
        style = ttk.Style(self)
        style.configure("Title.TLabel", font=("Segoe UI", 50, "bold"))
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure("TLabel", font=("Segoe UI", 10))

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background="#ّF3F6FA")
        style.configure("TLabel", background="#F3F6FA", foreground="#243247")
        style.configure("TLabelframe", background="#FFFFFF")
        style.configure("TLabelframe.Label", background="#FF6692", foreground="#442269", font=("Segoe UI", 11, "bold"))
        style.configure("TEntry", padding=6)
        style.configure("TButton", padding=8, background="#46637C", foreground="#F6EDFF")
        style.map("TButton", background=[("active", "#1D4ED8")])

        self.update_idletasks()
        self.base_width = self.winfo_width()
        self.base_height = self.winfo_height()
        self.bind("<Configure>", self.resize_widgets)

    def widget_form(self):

        LabelFrame1 = ttk.LabelFrame(self, text = "Form")
        LabelFrame1.pack(padx = 10, pady = 10, fill = "both",)

        label1 = ttk.Label(LabelFrame1, text="name product:")
        self.entry1 = ttk.Entry(LabelFrame1, validate="key", validatecommand=(self.register(Security.checker), "%P"))
        label1.grid( row = 0, column = 0, padx = 1, pady = 1, sticky="ew")
        self.entry1.grid( row = 0, column = 1, padx = 5, pady = 5, sticky="ew")
        label2 = ttk.Label(LabelFrame1, text="number_of_exist")
        self.entry2 = ttk.Entry(LabelFrame1, validate="key", validatecommand=(self.register(Security.checker_integer), "%P"))
        label2.grid( row = 1, column = 0, padx = 5, pady = 5, sticky="ew")
        self.entry2.grid( row = 1, column = 1, padx = 5, pady = 5, sticky="ew")
        label3 = ttk.Label(LabelFrame1, text = "price")
        self.entry3 = ttk.Entry(LabelFrame1, validate="key", validatecommand=(self.register(Security.checker_price), "%P"))
        label3.grid( row = 2, column = 0, padx = 5, pady = 5, sticky="ew")
        self.entry3.grid( row = 2, column = 1, padx = 5, pady = 5, sticky="ew")
    
    def widget_print(self):
        Labelframe3 = ttk.LabelFrame(self, text="Print")
        Labelframe3.pack(padx=10, pady=10, fill="both", side = "right")
    
        self.output = tk.Text(Labelframe3, height=12, width=70)
        self.output.pack(fill="both", expand=True, padx=5, pady=5)

    def widget_menu(self):
        LabelFrame2 = ttk.LabelFrame(self, text = "Menu")
        LabelFrame2.pack(padx = 10, pady = 10, fill = "both")
        button_1 = ttk.Button(LabelFrame2, text = "Append", command = lambda: Table_products.append(self.entry1.get(), self.entry2.get(), self.entry3.get()), width = 50, )
        button_2 = ttk.Button(LabelFrame2, text = "Erase", command = lambda: Table_products.erase(self.entry1.get()), width = 50)
        button_3 = ttk.Button(LabelFrame2, text = "Modify", command = lambda: Table_products.modify(self.entry1.get(), self.entry2.get(), self.entry3.get()), width = 50)
        button_4 = ttk.Button(LabelFrame2, text = "Find", command = self.find_product, width = 50)
        button_5 = ttk.Button(LabelFrame2, text = "CSV_Backup", command = lambda: Table_products.csv_backup(), width = 50)
        button_1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="ew")
        button_2.grid(row = 1, column = 0, padx = 5, pady = 5, sticky="ew")
        button_3.grid(row = 2, column = 0, padx = 5, pady = 5, sticky="ew")
        button_4.grid(row = 3, column = 0, padx = 5, pady = 5, sticky="ew")
        button_5.grid(row = 4, column = 0, padx = 5, pady = 5, sticky="ew")
    
    def show_product(self, rows):
        self.output.delete("1.0", tk.END)
        if not rows:
            self.output.insert(tk.END, "product not find")
            return
    
        for row in rows:
            self.output.insert(tk.END, f"{row[1]} | {row[2]} | {row[3]} \n")
    
    def find_product(self):
        rows = Table_products.find(self.entry1.get())
        self.show_product(rows)

    def resize_widgets(self, event):
        if event.widget is not self:
            return

        scale = min(event.width / self.base_width, event.height / self.base_height)

        for widget in self.winfo_children():
            self.resize_widget(widget, scale)

    def resize_widgets(self, event):
        if event.widget is not self:
            return

        scale_x = event.width / self.base_width
        scale_y = event.height / self.base_height
        scale = min(scale_x, scale_y)

        font_size = max(8, int(10 * scale))
        entry_width = max(10, int(20 * scale))
        button_width = max(10, int(15 * scale))
        
class Run_invoice_customer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.minsize(750, 500)
        self.title("Invoice Customer")
        style = ttk.Style(self)
        style.configure("Title.TLabel", font=("Segoe UI", 50, "bold"))
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure("TLabel", font=("Segoe UI", 10))

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background="#ّF3F6FA")
        style.configure("TLabel", background="#F3F6FA", foreground="#243247")
        style.configure("TLabelframe", background="#FFFFFF")
        style.configure("TLabelframe.Label", background="#FF6692", foreground="#442269", font=("Segoe UI", 11, "bold"))
        style.configure("TEntry", padding=6)
        style.configure("TButton", padding=8, background="#46637C", foreground="#F6EDFF")
        style.map("TButton", background=[("active", "#1D4ED8")])

        self.update_idletasks()
        self.base_width = self.winfo_width()
        self.base_height = self.winfo_height()
        self.bind("<Configure>", self.resize_widgets)

    def widget_form(self):

        LabelFrame1 = ttk.LabelFrame(self, text = "Form")
        LabelFrame1.pack(padx = 10, pady = 10, fill = "both",)

        fields = [
            ("invoice number:", "invoice"), ("first name:", "first"),
            ("last name:", "last"), ("customer phone:", "phone"),
            ("total amount:", "amount"), ("date (YYYY-MM-DD):", "date"),
            ("start date:", "start"), ("end date:", "end"),
        ]
        self.invoice_entries = {}
        for index, (caption, key) in enumerate(fields):
            row, col = divmod(index, 2)
            ttk.Label(LabelFrame1, text=caption).grid(row=row, column=col * 2, padx=5, pady=5, sticky="ew")
            entry = ttk.Entry(LabelFrame1)
            entry.grid(row=row, column=col * 2 + 1, padx=5, pady=5, sticky="ew")
            self.invoice_entries[key] = entry

        
        self.entry1 = self.invoice_entries["invoice"]
        self.entry2 = self.invoice_entries["phone"]
        self.entry3 = self.invoice_entries["amount"]
        self.entry4 = self.invoice_entries["date"]
        self.entry5 = self.invoice_entries["start"]
        self.entry6 = self.invoice_entries["end"]

    def save_invoice(self, modify=False):
        values = self.invoice_entries
        invoice = values["invoice"].get().strip()
        first = values["first"].get().strip()
        last = values["last"].get().strip()
        phone = values["phone"].get().strip()
        date = values["date"].get().strip()
        try:
            amount = float(values["amount"].get().strip())
        except ValueError:
            messagebox.showerror("Invalid amount", "Total amount must be a number.")
            return
        if not invoice or not phone or not date:
            messagebox.showerror("Missing information", "Invoice number, customer phone, and date are required.")
            return
        if modify:
            Table_invoice_customer.modify(invoice, first, last, phone, amount, date)
        else:
            Table_invoice_customer.append(invoice, first, last, phone, amount, date)

    def widget_print(self):
        Labelframe3 = ttk.LabelFrame(self, text="Print")
        Labelframe3.pack(padx=10, pady=10, fill="both", side = "right")
        
        self.output = tk.Text(Labelframe3, height=12, width=70)
        self.output.pack(fill="both", expand=True, padx=5, pady=5)

    def widget_menu(self):
        LabelFrame2 = ttk.LabelFrame(self, text = "Menu")
        LabelFrame2.pack(padx=10,pady=10,fill="both")
        button_1 = ttk.Button(LabelFrame2, text = "Append", command = self.save_invoice, width = 50)
        button_2 = ttk.Button(LabelFrame2, text = "Erase", command = lambda: Table_invoice_customer.erase(self.entry1.get()), width = 50)
        button_3 = ttk.Button(LabelFrame2, text = "Modify", command = lambda: self.save_invoice(modify=True), width = 50)
        button_4 = ttk.Button(LabelFrame2, text = "Find", command = self.find_invoice, width = 50)
        button_5 = ttk.Button(LabelFrame2, text = "CSV_Backup", command = lambda: Table_invoice_customer.csv_backup(), width = 50)
        button_6 = ttk.Button(LabelFrame2, text = "Find By Date", command  = self.search_invoices_by_date, width = 50)
        button_1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="ew")
        button_2.grid(row = 1, column = 0, padx = 5, pady = 5, sticky="ew")
        button_3.grid(row = 2, column = 0, padx = 5, pady = 5, sticky="ew")
        button_4.grid(row = 3, column = 0, padx = 5, pady = 5, sticky="ew")
        button_5.grid(row = 4, column = 0, padx = 5, pady = 5, sticky="ew")
        button_6.grid(row = 5, column = 0, padx = 5, pady = 5, sticky="ew")
    
    def show_invoice(self, rows):
        self.output.delete("1.0", tk.END)
        if not rows:
            self.output.insert(tk.END, "invoice not find")
            return
        
        for row in rows:
            self.output.insert(tk.END, f"Invoice: {row[1]} | {row[2]} {row[3]} | Phone: {row[4]} | Total: {row[5]} | Date: {row[6]}\n")
        
    def find_invoice(self):
        rows = Table_invoice_customer.find(self.entry1.get())
        self.show_invoice(rows)

    def search_invoices_by_date(self):
        rows = Table_invoice_customer.find_between_dates(self.entry5.get(),self.entry6.get())
        self.show_invoice(rows)

    def resize_widgets(self, event):
        if event.widget is not self:
            return

        scale = min(event.width / self.base_width, event.height / self.base_height)

        for widget in self.winfo_children():
            self.resize_widget(widget, scale)

    def resize_widgets(self, event):
        if event.widget is not self:
            return

        scale_x = event.width / self.base_width
        scale_y = event.height / self.base_height
        scale = min(scale_x, scale_y)

        font_size = max(8, int(10 * scale))
        entry_width = max(10, int(20 * scale))
        button_width = max(10, int(15 * scale))
        





