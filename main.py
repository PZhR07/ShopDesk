from GUI import Run_contact, Run_product, Run_invoice_customer
import tkinter as tk
from tkinter import ttk
from Shop import Shop


class Start(tk.Tk):

    def __init__(self):
        super().__init__()
        self.minsize(225, 150)
        self.title("App Selector")

        label_frame = ttk.LabelFrame(self, text="Application")
        label_frame.pack(padx=10, pady=10, fill="both")
        message = tk.Label(label_frame, text="Please choose which APP you want to use:")
        message.pack(padx=10, pady=5)

        ttk.Button(label_frame, text="Shop", command=self.st1).pack(padx=10, pady=5, fill="x")
        ttk.Button(label_frame, text="Database", command=self.st).pack(padx=10, pady=5, fill="x")

    def st(self):
        self.destroy()
        GUI_runner().mainloop()

    def st1(self):
        self.destroy()
        Shop_runner().run()




class GUI_runner(tk.Tk):

    def __init__(self):
        super().__init__()
        self.minsize(225, 150)
        self.title("App Selector")

        label_frame = ttk.LabelFrame(self, text="Application")
        label_frame.pack(padx=10, pady=10, fill="both")
        message = tk.Label(label_frame, text="Please choose which database you want to use:")
        message.pack(padx=10, pady=5)

        button1 = ttk.Button(label_frame, text="Contact", command=self.runner_contact)
        button2 = ttk.Button(label_frame, text="Product", command=self.runner_product)
        button3 = ttk.Button(label_frame, text="Invoice", command=self.runner_invoice)
        
        button1.pack(padx=10, pady=5, fill="x")
        button2.pack(padx=10, pady=5, fill="x")
        button3.pack(padx=10, pady=5, fill="x")
        

    def runner(self, runner) -> None:
        runner.widget_form()
        runner.widget_print()
        runner.widget_menu()
        runner.mainloop()

    def runner_contact(self) -> None:
        self.runner(Run_contact())
        
    def runner_product(self) -> None:
        self.runner(Run_product())

    def runner_invoice(self) -> None:
        self.runner(Run_invoice_customer())



class Shop_runner:
    def run(self):
        shop = Shop()
        shop.product()
        shop.mainloop()








start = Start()

start.mainloop()


