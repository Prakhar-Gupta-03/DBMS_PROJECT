import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget

class admin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel("Admin")
        layout.addWidget(self.label)
        self.view_products_button = QPushButton("View Products")
        self.view_products_button.move(50, 200)
        layout.addWidget(self.view_products_button)
        self.view_categories_button = QPushButton("View Categories")
        self.view_categories_button.move(150, 200)
        layout.addWidget(self.view_categories_button)
        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.move(250, 200)
        layout.addWidget(self.add_product_button)
        self.add_category_button = QPushButton("Add Category")
        self.add_category_button.move(350, 200)
        layout.addWidget(self.add_category_button)
        self.remove_product_button = QPushButton("Remove Product")
        self.remove_product_button.move(450, 200)
        layout.addWidget(self.remove_product_button)
        self.remove_category_button = QPushButton("Remove Category")
        self.remove_category_button.move(550, 200)
        layout.addWidget(self.remove_category_button)
        self.change_price_product_button = QPushButton("Change Price of Product")
        self.change_price_product_button.move(650, 200)
        layout.addWidget(self.change_price_product_button)
        self.change_quantity_product_button = QPushButton("Change Quantity of Product")
        self.change_quantity_product_button.move(750, 200)
        layout.addWidget(self.change_quantity_product_button)
        self.change_pass_button = QPushButton("Change Password")
        self.change_pass_button.move(850, 200)
        layout.addWidget(self.change_pass_button)
        self.back_button = QPushButton("Back")
        self.back_button.move(950, 200)
        layout.addWidget(self.back_button)
        self.exit_button = QPushButton("Exit")
        self.exit_button.move(1050, 200)
        layout.addWidget(self.exit_button)


    #     button click events:
        self.exit_button.clicked.connect(self.exit_application)


    #     buttons functions:

    def exit_application(self):
        QApplication.quit()
