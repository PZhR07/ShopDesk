import re
import sqlite3 as sql
import datetime
import shutil
from tkinter import *
from tkinter import messagebox
import csv
from persiantools.jdatetime import JalaliDate

class Security:
    
    @staticmethod
    def checker(value):
        return value == "" or re.fullmatch(r"[A-Za-zآ-ی ]+", value) is not None

    @staticmethod
    def checker_phone(value):
        return value == "" or re.fullmatch(r"[0-9]{0,11}", value) is not None

    @staticmethod
    def valid_phone(value):
        return re.fullmatch(r"[0-9]{11}", value) is not None

    @staticmethod
    def checker_integer(value):
        return value == "" or re.fullmatch(r"[0-9]+", value) is not None

    @staticmethod
    def checker_price(value):
        return value == "" or re.fullmatch(r"[0-9]+(\.[0-9]*)?", value) is not None

    @staticmethod
    def checker_date(value):
        return value == "" or re.fullmatch(r"[0-9]{0,4}(-[0-9]{0,2}){0,2}", value) is not None


class Sql_checker:

    allowed_commands = [
                        """CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, number TEXT UNIQUE, date TEXT)""",
                        """INSERT INTO contact(first_name, last_name, number, date) VALUES (?, ?, ?, ?)""",
                        """DELETE FROM contact WHERE number = ?""",
                        """UPDATE contact SET last_name = ?, number = ? WHERE first_name = ?""",
                        """SELECT * FROM contact WHERE last_name = ? OR number = ?""",
                        """SELECT * FROM contact""",
                        """SELECT first_name, last_name FROM contact WHERE number = ?""",

                        """CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name_product TEXT, number_of_exist INTEGER, price TEXT)""",
                        """INSERT INTO products(name_product, number_of_exist, price) VALUES(?, ?, ?)""",
                        """DELETE FROM products WHERE name_product = ?""",
                        """UPDATE products SET number_of_exist = ?, price = ? WHERE name_product = ?""",
                        """SELECT * FROM products WHERE name_product = ?""",
                        """SELECT * FROM products""",
                        """SELECT id, name_product, number_of_exist FROM products ORDER BY name_product""",
                        """SELECT number_of_exist, price FROM products WHERE name_product = ?""",
                        """UPDATE products SET number_of_exist = number_of_exist - ? WHERE id = ? AND number_of_exist >= ?""",
                        """UPDATE products SET number_of_exist = number_of_exist - ? WHERE name_product = ? AND number_of_exist >= ?""",

                        """CREATE TABLE IF NOT EXISTS invoice_customer(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_number TEXT, first_name TEXT, last_name TEXT, customer_number TEXT, total_amount REAL, date TEXT)""",
                        """INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES(?, ?, ?, ?, ?, ?)""",
                        """DELETE FROM invoice_customer WHERE invoice_number = ?""",
                        """UPDATE invoice_customer SET first_name = ?, last_name = ?, customer_number = ?, total_amount = ?, date = ? WHERE invoice_number = ?""",
                        """SELECT * FROM invoice_customer WHERE invoice_number = ?""",
                        """SELECT * FROM invoice_customer WHERE date BETWEEN ? AND ? ORDER BY date""",
                        """SELECT * FROM invoice_customer""",
                        """UPDATE invoice_customer SET total_amount = ? WHERE invoice_number = ?""",

                        """CREATE TABLE IF NOT EXISTS invoice_items(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_id INTEGER, product_name TEXT, quantity INTEGER, unit_price REAL, line_total REAL)""",
                        """INSERT INTO invoice_items(invoice_id, product_name, quantity, unit_price, line_total) VALUES (?, ?, ?, ?, ?)""",
                        """CREATE TABLE IF NOT EXISTS invoice_customer(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_number TEXT, first_name TEXT, last_name TEXT, customer_number TEXT, total_amount REAL, date TEXT)""",
                        """CREATE TABLE IF NOT EXISTS invoice_items(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_id INTEGER, product_name TEXT, quantity INTEGER, unit_price REAL, line_total REAL)""",
                        """INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES (?, ?, ?, ?, ?, ?)""",
                        """INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES (?, ?, ?, ?, ?, ?)""",
                        """CREATE TABLE IF NOT EXISTS invoice_items(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_id INTEGER, product_name TEXT, quantity INTEGER, unit_price REAL, line_total REAL)""",
                        """CREATE TABLE IF NOT EXISTS invoice_customer(id INTEGER PRIMARY KEY AUTOINCREMENT, invoice_number TEXT, first_name TEXT, last_name TEXT, 
        customer_number TEXT, total_amount REAL, date TEXT)""",
        """INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES(?, ?, ?, ?, ?, ?)""",
"""INSERT INTO invoice_customer(invoice_number, first_name, last_name, customer_number, total_amount, date) VALUES (?, ?, ?, ?, ?, ?)""",
"""CREATE TABLE IF NOT EXISTS invoice_items(id INTEGER PRIMARY KEY AUTOINCREMENT, 
        invoice_id INTEGER, product_name TEXT, quantity INTEGER, unit_price REAL, line_total REAL)""",]

    @staticmethod
    def check_command(cmd):
        if cmd in Sql_checker.allowed_commands:
            return True
        else:
            raise ValueError("Invalid SQL command. Please use one of the allowed commands.")

    @staticmethod
    def constructor(cmd: str, data=()):
        try:
            Sql_checker.check_command(cmd)

            with sql.connect("database.db") as conn:
                conn.execute("PRAGMA foreign_keys = ON")
                cur = conn.cursor()
                cur.execute(cmd, data)

                if cur.description:
                    rows = cur.fetchall()
                    title = [i[0] for i in cur.description]
                    return title, rows

                conn.commit()
                return True

        except (sql.Error, ValueError) as error:
            messagebox.showerror("Database Error", str(error))
            return False
