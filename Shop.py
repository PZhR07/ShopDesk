import datetime
import tkinter as tk
from tkinter import messagebox, ttk
from Security import Sql_checker
from persiantools.jdatetime import JalaliDate

class Shop(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Shop")
        self.minsize(650, 400)
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

    def product(self):
        cmd = """SELECT id, name_product, number_of_exist FROM products ORDER BY name_product"""
        result = Sql_checker.constructor(cmd)
        if result is False:
            return
        title, data = result

        menu = ttk.LabelFrame(self, text="Products")
        menu.pack(padx=10, pady=10, fill="both", expand=True)

        
        menu.columnconfigure(2, weight=2)

        Label_1 = ttk.Label(menu, text="Product", style="Header.TLabel")
        Label_2 = ttk.Label(menu, text="Stock", style="Header.TLabel")
        Label_3 = ttk.Label(menu, text="Purchase Quantity", style="Header.TLabel")

        Label_1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        Label_2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        Label_3.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.entries = {}

        for i, (product_id, product_name, stock) in enumerate(data, start=1):

            label = ttk.Label(menu, text=product_name, width = 20)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="ew")

            label_1 = ttk.Label(menu, text = stock)
            label_1.grid(row=i, column=1, padx=5, pady=5, sticky="ew")

            entry = ttk.Entry(menu, width=20)
            entry.grid(row=i, column=2, padx=5, pady=5, sticky="ew")
            self.entries[product_name] = entry

        Label_4 = ttk.Label(menu, text = "number:")
        Label_4.grid(row = len(data) + 1, column = 0, padx=5, pady=5, sticky="ew")
        self.entry_1 = ttk.Entry(menu)
        self.entry_1.grid(row = len(data) + 1, column = 2, padx=5, pady=5, sticky="ew")


        button = ttk.Button(menu, text="PRESS", command=self.press)
        button.grid(row=len(data) + 2, column=0, columnspan=10, pady=10, sticky="ew")

    def increase(self):
        for product_id, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                continue

            try:
                quantity = int(value)
            except ValueError:
                messagebox.showerror("Invalid Quantity", "Quantity must be a whole number.")
                return

            if quantity <= 0:
                messagebox.showerror("Invalid Quantity", "Quantity must be greater than zero.")
                return

            cmd = """UPDATE products SET number_of_exist = number_of_exist - ? WHERE id = ? AND number_of_exist >= ?"""
            result = Sql_checker.constructor(cmd, (quantity, product_id, quantity))

            if result is False:
                return

    def create_join_invoice(self):
        customer_number = self.entry_1.get().strip()

        if not customer_number:
            messagebox.showerror("Invalid Customer", "Enter the customer's phone number.")
            return

        result = Sql_checker.constructor("""SELECT first_name, last_name FROM contact WHERE number = ?""",(customer_number,))

        if result is False:
            return

        columns, rows = result

        if not rows:
            messagebox.showerror("Customer Not Found", "No customer has this phone number.")
            return

        first_name, last_name = rows[0]
        invoice_number = datetime.datetime.now().strftime("INV%Y%m%d%H%M%S%f")
        invoice_date = JalaliDate(datetime.datetime.now()).to_gregorian()


        data = (invoice_number, first_name, last_name, customer_number, 0, invoice_date)
        invoice_id = Sql_checker.constructor("""INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES (?, ?, ?, ?, ?, ?)""", data)

        if invoice_id is False:
            return

        total_amount = 0
        has_items = False

        for product_name, entry in self.entries.items():
            value = entry.get().strip()

            if not value:
                continue

            if not value.isdigit() or int(value) <= 0:
                messagebox.showerror("Invalid Quantity", "Enter a whole number greater than zero.")
                return

            quantity = int(value)

            result = Sql_checker.constructor("""SELECT number_of_exist, price FROM products WHERE name_product = ?""",(product_name,))

            if result is False:
                return

            columns, rows = result

            if not rows:
                messagebox.showerror("Product Not Found", f"Product {product_name} was not found.")
                return

            stock, price = rows[0]

            if quantity > stock:
                messagebox.showerror("Insufficient Stock", f"Not enough stock for {product_name}.")
                return

            unit_price = float(price)
            line_total = quantity * unit_price

            data = (invoice_id, product_name, quantity, unit_price, line_total)
            result = Sql_checker.constructor("""INSERT INTO invoice_items(invoice_id, product_name, quantity, unit_price, line_total) VALUES (?, ?, ?, ?, ?)""", data)

            if result is False:
                return

            data = (quantity, product_name, quantity)
            result = Sql_checker.constructor("""UPDATE products SET number_of_exist = number_of_exist - ? WHERE name_product = ? AND number_of_exist >= ?""", data)

            if result is False:
                return

            total_amount += line_total
            has_items = True

        if not has_items:
            messagebox.showerror("No Products", "Enter a quantity for at least one product.")
            return

        data = (total_amount, invoice_number)
        result = Sql_checker.constructor("""UPDATE invoice_customer SET total_amount = ? WHERE invoice_number = ?""",data)

        if result is False:
            return

        messagebox.showinfo("Success", f"Invoice {invoice_number} was created.")

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

        for widget in self.winfo_children():
            self.resize_children(widget, font_size, entry_width, button_width)

    def resize_children(self, parent, font_size, entry_width, button_width):
        for widget in parent.winfo_children():
            if isinstance(widget, (tk.Label, ttk.Label, ttk.Button, ttk.Entry)):
                widget.configure(font=("Segoe UI", font_size))

            if isinstance(widget, ttk.Entry):
                widget.configure(width=entry_width)

            if isinstance(widget, ttk.Button):
                widget.configure(width=button_width)

            self.resize_children(widget, font_size, entry_width, button_width)

    def press(self):
        self.create_join_invoice()
        self.increase()













        