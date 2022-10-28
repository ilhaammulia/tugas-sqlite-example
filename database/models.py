import sqlite3
import os


class DB:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def createDatabase(self):
        try:
            connection = sqlite3.connect(self.base_path + "/database.db")
            cursor = connection.cursor()
            cursor.execute(
                """CREATE TABLE products (id integer primary key AUTOINCREMENT, name varchar(20) UNIQUE, type varchar(10), stock int(11));""")
            connection.commit()
            print("SQLite Database Created.")
            cursor.close()
        except sqlite3.Error as e:
            print("Error while creating database", e)
        finally:
            if connection:
                connection.close()

    def getProducts(self):
        try:
            connection = sqlite3.connect(self.base_path + "/database.db")
            cursor = connection.cursor()
            get = cursor.execute("SELECT * FROM products").fetchall()
            return get
        except sqlite3.Error as e:
            print("Error while fetching products:", e)

    def addProducts(self, product_name, product_type, product_stock):
        try:
            connection = sqlite3.connect(self.base_path + "/database.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products(name, type, stock) VALUES (?, ?, ?)",
                           (product_name, product_type, product_stock))
            connection.commit()
            cursor.close()
            return "Product berhasil ditambahkan."
        except sqlite3.Error:
            return "Product gagal ditambahkan"
        finally:
            if connection:
                connection.close()

    def removeProducts(self, product_id):
        try:
            connection = sqlite3.connect(self.base_path + "/database.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
            connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print("Error when remove product", e)
        finally:
            if connection:
                connection.close()
