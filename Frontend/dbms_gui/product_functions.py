import sys

from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget, \
    QTableView, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import mysql.connector
import functions
class add_product(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.name_label = QLabel("Product Name:", self)
        self.name_label.move(50, 50)
        self.name_edit = QLineEdit(self)
        self.name_edit.move(150, 50)

        self.price_label = QLabel("Product Price:", self)
        self.price_label.move(50, 100)
        self.price_edit = QLineEdit(self)
        self.price_edit.move(150, 100)
        self.quan_label = QLabel("Enter product quantity:", self)
        self.quan_label.move(50, 150)
        self.quantity_edit = QLineEdit(self)
        self.quantity_edit.move(150, 150)
        self.category_label = QLabel("Enter product category:", self)
        self.category_label.move(50, 200)
        self.category_edit = QLineEdit(self)
        self.category_edit.move(150, 200)
        self.add_p_in_product = QPushButton("Add Product", self)
        self.add_p_in_product.move(50, 250)
        self.add_p_in_product.clicked.connect(self.save_details)
        self.back_button = QPushButton("Back", self)
        self.back_button.move(150, 350)
    def save_details(self):
        # print("save_details")
        name = self.name_edit.text()
        # print(name)
        price = self.price_edit.text()
        quantity = self.quantity_edit.text()
        category = self.category_edit.text()
        # print(name, price, quantity, category)
        if name == "" or price == "" or quantity == "" or category == "":
            QMessageBox.warning(self, "Error", "Please fill all the fields")
        else:
            # print(name, price, quantity, category)
            functions.add_product_func(self,name, price, quantity, category)
            QMessageBox.information(self, "Success", "Product added successfully")
            self.name_edit.setText("")
            self.price_edit.setText("")
            self.quantity_edit.setText("")
            self.category_edit.setText("")
class remove_product(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.price_label = QLabel("Product ID:", self)
        self.price_label.move(50, 100)
        self.price_edit = QLineEdit(self)
        self.price_edit.move(150, 100)
        self.add_p_in_product = QPushButton("Delete Product", self)
        self.add_p_in_product.move(50, 250)
        self.add_p_in_product.clicked.connect(self.save_details)
        self.back_button = QPushButton("Back", self)
        self.back_button.move(150, 350)
    def save_details(self):
        # print("save_details")
        id = self.price_edit.text()
        # print(name, price, quantity, category)
        if id == "":
            QMessageBox.warning(self, "Error", "Please fill all the fields")
        else:
            # print(name, price, quantity, category)
            functions.remove_product_func(self, id)
            QMessageBox.information(self, "Success", "Product deleted successfully")
            self.name_edit.setText("")
        # self.delete_button = QPushButton("Delete Product", self)
        # self.delete_button.move(200, 150)
        # self.delete_button.clicked.connect(self.delete_product)
class change_price(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.id_label = QLabel("Product ID:", self)
        self.id_label.move(50, 50)
        self.id_edit = QLineEdit(self)
        self.id_edit.move(150, 50)
        self.price_label = QLabel("Product new Price:", self)
        self.price_label.move(50, 100)
        self.price_edit = QLineEdit(self)
        self.price_edit.move(150, 100)
        self.add_p_in_product = QPushButton("Change Price", self)
        self.add_p_in_product.move(50, 250)
        self.add_p_in_product.clicked.connect(self.save_details)
        self.back_button = QPushButton("Back", self)
        self.back_button.move(150, 350)
    def save_details(self):
        price = self.price_edit.text()
        id = self.id_edit.text()
        print(id, price)
        if self.id_edit.text() == "" or self.price_edit.text() == "":
            QMessageBox.warning(self, "Error", "Please fill all the fields")
        else:
            print(id, price)
            functions.change_price_func(self,id,price)
            QMessageBox.information(self, "Success", "Price changed successfully")
            self.id_edit.setText("")
            self.price_edit.setText("")

class change_quantity(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.id_label = QLabel("Product ID:", self)
        self.id_label.move(50, 50)
        self.id_edit = QLineEdit(self)
        self.id_edit.move(150, 50)
        self.quan_label = QLabel("Product new Quantity:", self)
        self.quan_label.move(50, 100)
        self.quan_edit = QLineEdit(self)
        self.quan_edit.move(150, 100)
        self.add_p_in_product = QPushButton("Change quantity", self)
        self.add_p_in_product.move(50, 250)
        self.add_p_in_product.clicked.connect(self.save_details)
        self.back_button = QPushButton("Back", self)
        self.back_button.move(150, 350)
    def save_details(self):
        quantity = self.quan_edit.text()
        id = self.id_edit.text()
        # print(id, quantity)
        if self.id_edit.text() == "" or self.quan_edit.text() == "":
            QMessageBox.warning(self, "Error", "Please fill all the fields")
        else:
            # print(id, quantity)
            functions.change_quan_func(self,id,quantity)
            QMessageBox.information(self, "Success", "Quantity changed successfully")
            self.id_edit.setText("")
            self.quan_edit.setText("")
class add_category(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.name_label = QLabel("Category name:", self)
        self.name_label.move(50, 50)
        self.name_edit = QLineEdit(self)
        self.name_edit.move(150, 50)
        self.add_cat_button = QPushButton("Add Category", self)
        self.add_cat_button.move(50, 250)
        self.add_cat_button.clicked.connect(self.save_details)
        self.back_button = QPushButton("Back", self)
        self.back_button.move(150, 350)
    def save_details(self):
        name = self.name_edit.text()
        if self.name_edit.text() == "":
            QMessageBox.warning("Error", "Please fill all the fields")
        else:
            functions.add_category_func(self,name)
            QMessageBox.information(self, "Success", "Category added successfully")
            self.name_edit.setText("")


