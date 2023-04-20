import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QStackedWidget
from main_menu import main_menu
from customer import customer
from admin import admin
from product_functions import add_product, remove_product,change_price,change_quantity,add_category
import functions
import mysql.connector

class MainWindow(QMainWindow):
#     online retail store
    def __init__(self):
        super().__init__()


        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        #create the screens
        self.main_menu = main_menu()
        self.customer_menu = customer()
        self.admin_menu = admin()
        self.add_product = add_product()
        self.remove_product = remove_product()
        self.change_price = change_price()
        self.change_quantity = change_quantity()
        self.add_category = add_category()
        #add them to the QStackedWidget
        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.customer_menu)
        self.stacked_widget.addWidget(self.admin_menu)
        self.stacked_widget.addWidget(self.add_product)
        self.stacked_widget.addWidget(self.remove_product)
        self.stacked_widget.addWidget(self.change_price)
        self.stacked_widget.addWidget(self.change_quantity)
        self.stacked_widget.addWidget(self.add_category)


        # Connect the button signals to the slot that changes the current widget
        self.main_menu.customer_menu_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.customer_menu))
        self.customer_menu.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_menu))
        self.main_menu.admin_menu_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.admin_menu))
        self.admin_menu.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_menu))
        self.admin_menu.view_products_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(functions.view_products(self).show()))
        self.admin_menu.view_categories_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(functions.view_categories(self).show()))
        self.admin_menu.remove_product_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.remove_product))
        # self.admin_menu.remove_category_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.remove_product))
        self.admin_menu.add_product_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_product))
        self.remove_product.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.admin_menu))
        self.change_price.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.admin_menu))
        self.admin_menu.change_price_product_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.change_price))
        self.admin_menu.change_quantity_product_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.change_quantity))
        self.change_quantity.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.admin_menu))
        self.add_category.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.admin_menu))
        self.admin_menu.add_category_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_category))
        self.add_product.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.admin_menu))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
