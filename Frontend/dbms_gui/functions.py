from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QLabel, \
    QLineEdit
import mysql.connector
# connect to database



def exit_application(self):
    QApplication.quit()

def view_products(self):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product")
    res = cursor.fetchall()
    self.table = QTableWidget()
    self.setCentralWidget(self.table)

    self.table.setRowCount(len(res))
    self.table.setColumnCount(6)
    self.table.setHorizontalHeaderLabels(["Product_ID", "Product_name", "Product_price", "Product_quantity", "Category_ID", "Admin_ID"])

    print(len(res))
    print(res)
    for i in range(0, len(res)):
        for j in range(0, 6):
            print(res[i][j])
            self.table.setItem(i,j,QTableWidgetItem(res[i][j]))
    return self.table
def view_categories(self):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM category")
    res = cursor.fetchall()
    self.table = QTableWidget()
    self.setCentralWidget(self.table)

    self.table.setRowCount(len(res))
    self.table.setColumnCount(3)
    self.table.setHorizontalHeaderLabels(["Admin_ID", "Category_ID", "Category_name"])

    print(len(res))
    print(res)
    for i in range(0, len(res)):
        for j in range(0,3):
            print(res[i][j])
            self.table.setItem(i,j,QTableWidgetItem(res[i][j]))
    return self.table


def add_product_func(self,name,price,quantity,category):
    # print("in add product func")
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    Admin_ID = 1
    product_name = name
    product_price = price
    product_quantity = quantity
    Category_ID = category
    # product_name = input("Enter product name: ")
    # product_price = int(input("Enter product price: "))
    # product_quantity = int(input("Enter product quantity: "))
    # Category_ID = input("Enter product category: ")
    try:
        # print("till here")
        cursor.execute("insert into product (product_name, product_price, product_quantity, Category_ID, Admin_ID) values (%s, %s, %s, %s, %s)",
            (product_name, product_price, product_quantity, Category_ID, Admin_ID,))
        db.commit()
        # print("Product added successfully")
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))

def add_category_func(self,name):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    Admin_ID = 1
    category_name = name
    # category_name = input("Enter category name: ")
    try:
        cursor.execute("insert into category (category_name,Admin_ID) values (%s, %s)", (category_name, Admin_ID,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))

def change_price_func(self,id,price):
    print("in change price func")
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    product_id = id
    product_price = price
    print(product_id)
    cursor.execute("select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        try:
            cursor.execute("update product set product_price = %s where product_id = %s", (product_price, product_id,))
            db.commit()
        except:
            print("Bruh wtf!!!")
            # QMessageBox.about(self, "Success", "Price changed successfully")
            # print("Error: {}".format(err.msg))


def change_quan_func(self,id,quantity):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    product_id = id
    product_quantity = quantity
    cursor.execute("select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        try:
            cursor.execute("update product set product_quantity = %s where product_id = %s", (product_quantity, product_id,))
            db.commit()
        except:
            print("Bruh wtf!!!")









def remove_product_func(self,product_id):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    product_id = product_id
    # check if product exists
    cursor.execute("select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        # remove the product from the cart
        cursor.execute("delete from cart where product_id = %s", (product_id,))
        cursor.execute("delete from all_orders where product_id = %s", (product_id,))
        cursor.execute("delete from product where product_id = %s", (product_id,))
        db.commit()
        print("Product removed successfully")

def remove_category_func(self):
    db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
    cursor = db.cursor()
    category_name = input("Enter category name: ")
    # check if category exists
    cursor.execute("select category_id from category where category_name = %s", (category_name,))
    res = cursor.fetchall()
    print(res)
    if len(res) == 0:
        print("Error: Category does not exist")
    else:
        # remove all the products in the category
        # cursor.execute("select product_id from product where Category_ID = %s", (res[0][0],))
        # res = cursor.fetchall()
        for i in res:
            print(i[0])
        #     # remove the products from the cart
        #     cursor.execute("delete from cart where product_id = %s", (i[0],))
        #     cursor.execute("delete from all_orders where product_id = %s", (i[0],))
        #     cursor.execute("delete from product where product_id = %s", (i[0],))
        # remove the category
            cursor.execute("delete from category where category_id = %s", (i[0],))
        #     db.commit()
        print("Category removed successfully")

    # return self.table

    # for i in res:
    #     print("Product_ID: ", i[0])


# view_products(self=None)

# def view_products(self):
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM product")
#
#     # Create a standard item model
#     model = QStandardItemModel()
#     model.setHorizontalHeaderLabels(
#         ["Product_ID", "Product_name", "Product_price", "Product_quantity", "Category_ID", "Admin_ID"])
#
#     # Add the rows to the model using QStandardItem objects
#     for row_num, row_data in enumerate(cursor):
#         for col_num, col_data in enumerate(row_data):
#             item = QStandardItem(str(col_data))
#             model.setItem(row_num, col_num, item)
#
#     # Create a view and set its model
#     view = QTableView()
#     view.setModel(model)
#     main_window = QMainWindow()
#     main_window.setCentralWidget(view)
#     main_window.show()
#
#     # Create a back button and connect it to the main window's close event
#     back_button = QPushButton("Back", main_window)
#     back_button.move(10, 10)
#     back_button.clicked.connect(main_window.close)
#
#     # Start the main event loop
#     app = QApplication.instance()
#     app.exec_()
#
#     # Close the cursor and database connection
#     cursor.close()
#     db.close()
