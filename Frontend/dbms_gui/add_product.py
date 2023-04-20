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
        self.add_button = QPushButton("Add Product", self)
        self.add_button.move(50, 150)
        # self.add_button.clicked.connect(self.add_product)

        self.delete_button = QPushButton("Delete Product", self)
        self.delete_button.move(200, 150)
        # self.delete_button.clicked.connect(self.delete_product)


