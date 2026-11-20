import sqlite3 as sql
import datetime
import shutil
from tkinter import *
from tkinter import messagebox
import csv
from persiantools.jdatetime import JalaliDate
from Security import Sql_checker



class Table_contact:

    def first(self):
        cmd = """CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, number TEXT UNIQUE, date TEXT)"""
        Sql_checker.constructor(cmd)
        self.csv_backup_first()

    @staticmethod
    def append(first_name: str, last_name: str, number: str):
        cmd = """INSERT INTO contact(first_name, last_name, number, date) VALUES (?, ?, ?, ?)"""
        data = (first_name, last_name, number, JalaliDate(datetime.datetime.now()).to_gregorian())
        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return
        messagebox.showinfo(message = "APPENDED.")

    @staticmethod
    def erase(number:str):
        cmd = """DELETE FROM contact WHERE number = ?"""
        data = (number,)
        if messagebox.askyesno("Application", "Are you sure you want to delete?"):
            result = Sql_checker.constructor(cmd, data)
            if result is False:
                return
            messagebox.showinfo(message = "ERASED")

    @staticmethod
    def modify(first_name: str, last_name: str, number: str):
        cmd = """UPDATE contact SET last_name = ?, number = ? WHERE first_name = ?"""
        data = (last_name, number, first_name,)
        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return
        messagebox.showinfo(message = " MODIFIED")

    @staticmethod
    def find(last_name: str, number:str):
        cmd = """SELECT * FROM contact WHERE last_name = ? OR number = ?"""
        data1 = (last_name, number,)
        data = Sql_checker.constructor(cmd, data1)
        if  data is False:
            return

        if data is None:
            return []
        
        title, rows = data
        return rows

    @staticmethod
    def display_all():
        cmd = """SELECT * FROM contact"""
        data = Sql_checker.constructor(cmd)
        if data is False:
            return
        if data is None:
            return []

        title, rows = data
        return rows

    @staticmethod
    def backup():
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        mi = datetime.datetime.now().minute
        se = datetime.datetime.now().second
        try:
            shutil.copy(r"database.db", rf"C:\Users\Parsa\Desktop\Advance_Python\backups\backup_{y}_{m}_{d}_{h}_{mi}_{se}.db")
            messagebox.showinfo(message = "BACKUPED")
        except FileNotFoundError as error:
            messagebox.showerror(message = f"فایل مبدأ یا پوشهٔ مقصد پیدا نشد: {error}")
        except PermissionError as error:
            messagebox.showerror(message = f"اجازهٔ دسترسی وجود ندارد: {error}")
        except OSError as error:
            messagebox.showerror(message = f"خطا هنگام کپی فایل: {error}")

    def csv_backup_first(self):
        cmd = """SELECT * FROM contact"""
        data = Sql_checker.constructor(cmd)

        if data is None:
            return

        if data is False or data is None:
            return

        title, rows = data

        with open("csv_backup_contact.csv", "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(title)
            writer.writerows(rows)

    @staticmethod
    def csv_backup():

        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        mi = datetime.datetime.now().minute
        se = datetime.datetime.now().second
        try:
            shutil.copy(r"csv_backup_contact.csv", rf"C:\Users\Parsa\Desktop\Advance_Python\backups\csv_backup_contact_{y}_{m}_{d}_{h}_{mi}_{se}.csv")
            messagebox.showinfo(message="SAVED CSV")
        except FileNotFoundError as error:
            messagebox.showerror(message = f"فایل مبدأ یا پوشهٔ مقصد پیدا نشد: {error}")
        except PermissionError as error:
            messagebox.showerror(message = f"اجازهٔ دسترسی وجود ندارد: {error}")
        except OSError as error:
            messagebox.showerror(message = f"خطا هنگام کپی فایل: {error}")


class Table_products:

    def first(self):
        cmd = """CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name_product TEXT, number_of_exist INTEGER, price TEXT)"""
        Sql_checker.constructor(cmd)
        self.csv_backup_first()

    @staticmethod
    def append(name_product: str, number_of_exist: int, price: str):
        cmd = """INSERT INTO products(name_product, number_of_exist, price) VALUES(?, ?, ?)"""
        data = (name_product, number_of_exist, price,)
        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return
        messagebox.showinfo(message = "APPENDED.")

    @staticmethod
    def erase(name_product: str):
        cmd = """DELETE FROM products WHERE name_product = ?"""
        data =  (name_product,)
        if messagebox.askyesno("Application", "Are you sure you want to delete?"):
            result = Sql_checker.constructor(cmd, data)
            if result is False:
                return
            messagebox.showinfo(message = "ERASED")

    @staticmethod
    def modify(name_product: str, number_of_exist: int, price: str):
        cmd = """UPDATE products SET number_of_exist = ?, price = ? WHERE name_product = ?"""
        data = (number_of_exist, price, name_product)
        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return
        messagebox.showinfo(message = " MODIFIED")

    @staticmethod
    def find(name_product: str):
        cmd = """SELECT * FROM products WHERE name_product = ?"""
        data1 = (name_product,)
        data = Sql_checker.constructor(cmd, data1)
        if data is False:
            return
        
        if data is None:
            return []
               
        title, rows = data
        return rows

    
    def csv_backup_first(self):
        cmd = """SELECT * FROM products"""
        data = Sql_checker.constructor(cmd)
        if data is False:
            return
        if data is None:
            return 

        title, rows = data

        with open("csv_backup_product.csv", 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(title)
            writer.writerows(rows)

    @staticmethod
    def csv_backup():
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        mi = datetime.datetime.now().minute
        se = datetime.datetime.now().second
        try:
            shutil.copy(r"csv_backup_product.csv", rf"C:\Users\Parsa\Desktop\Advance_Python\backups\csv_backup_product_{y}_{m}_{d}_{h}_{mi}_{se}.csv")
            messagebox.showinfo(message="SAVED CSV")
        except FileNotFoundError as error:
            messagebox.showerror(message = f"فایل مبدأ یا پوشهٔ مقصد پیدا نشد: {error}")
        except PermissionError as error:
            messagebox.showerror(message = f"اجازهٔ دسترسی وجود ندارد: {error}")
        except OSError as error:
            messagebox.showerror(message = f"خطا هنگام کپی فایل: {error}")


class Table_invoice_customer:

    def first(self):
        cmd = """CREATE TABLE IF NOT EXISTS invoice_customer(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_number TEXT, first_name TEXT, last_name TEXT, 
        customer_number TEXT, total_amount REAL, date TEXT)"""
        Sql_checker.constructor(cmd)
        self.csv_backup_first()

    @staticmethod
    def append(invoice_number: str, first_name: str, last_name: str, customer_number: str, total_amount: float, date: str):
        cmd = """INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES(?, ?, ?, ?, ?, ?)"""
        data = (invoice_number, first_name, last_name, customer_number, total_amount, date)

        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return

        messagebox.showinfo(message="APPENDED.")

    @staticmethod
    def erase(invoice_number: str):
        cmd = """DELETE FROM invoice_customer WHERE invoice_number = ?"""
        data = (invoice_number,)
        if messagebox.askyesno("Application", "Are you sure you want to delete?"):
            result = Sql_checker.constructor(cmd, data)
            if result is False:
                return
            messagebox.showinfo(message="ERASED")

    @staticmethod
    def modify(invoice_number: str, first_name: str, last_name: str, customer_number: str, total_amount: float, date: str):
        cmd = """UPDATE invoice_customer SET first_name = ?, last_name = ?, customer_number = ?, total_amount = ?, date = ? WHERE invoice_number = ?"""
        data = (first_name, last_name, customer_number, total_amount, date, invoice_number)
        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return
        messagebox.showinfo(message="MODIFIED")

    @staticmethod
    def find(invoice_number: str):
        cmd = """SELECT * FROM invoice_customer WHERE invoice_number = ?"""
        data = (invoice_number,)
        result = Sql_checker.constructor(cmd, data)
        if result is False:
            return

        if result is None:
            return []

        title, rows = result
        return rows

    @staticmethod
    def find_between_dates(start_date, end_date):
        cmd = """SELECT * FROM invoice_customer WHERE date BETWEEN ? AND ? ORDER BY date"""
        result = Sql_checker.constructor(cmd, (start_date, end_date))

        if result is False:
            return

        if result is None:
            return []

        title, rows = result
        return rows

 
    def csv_backup_first(self):
        cmd = """SELECT * FROM invoice_customer"""
        data = Sql_checker.constructor(cmd)
        if data is False:
            return
        if data is None:
            return 

        title, rows = data

        with open("csv_backup_invoice.csv", 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(title)
            writer.writerows(rows)

        

    @staticmethod
    def csv_backup():
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        mi = datetime.datetime.now().minute
        se = datetime.datetime.now().second
        try:
            shutil.copy(r"csv_backup_invoice.csv", rf"C:\Users\Parsa\Desktop\Advance_Python\backups\csv_backup_invoice_{y}_{m}_{d}_{h}_{mi}_{se}.csv")
            messagebox.showinfo(message="SAVED CSV")
        except FileNotFoundError as error:
            messagebox.showerror(message = f"فایل مبدأ یا پوشهٔ مقصد پیدا نشد: {error}")
        except PermissionError as error:
            messagebox.showerror(message = f"اجازهٔ دسترسی وجود ندارد: {error}")
        except OSError as error:
            messagebox.showerror(message = f"خطا هنگام کپی فایل: {error}")


class Table_invoice_items:

    def first(self):
        cmd ="""CREATE TABLE IF NOT EXISTS invoice_items(id INTEGER PRIMARY KEY AUTOINCREMENT, 
        invoice_id INTEGER, product_name TEXT, quantity INTEGER, unit_price REAL, line_total REAL)"""
        Sql_checker.constructor(cmd)


con = Table_contact()
pro = Table_products()
inc = Table_invoice_customer()
ini = Table_invoice_items()


pro.first()
con.first()
inc.first()
ini.first()
