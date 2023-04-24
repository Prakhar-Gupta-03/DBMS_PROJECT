import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget
# this is the customer menu
class customer(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Customer Menu"
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        # create a button "View Products"
        layout = QVBoxLayout(self)
        self.view_products_button = QPushButton("View Products", self)
        self.view_products_button.move(50, 200)
        layout.addWidget(self.view_products_button)
        # create a button "View Categories"
        self.view_categories_button = QPushButton("View Categories", self)
        self.view_categories_button.move(150, 200)
        layout.addWidget(self.view_categories_button)
        # create a button "View Cart"
        self.view_cart_button = QPushButton("View Cart", self)
        self.view_cart_button.move(250, 200)
        layout.addWidget(self.view_cart_button)
        # create a button "add to cart"
        self.add_cart_button = QPushButton("Add to Cart", self)
        self.add_cart_button.move(350, 200)
        layout.addWidget(self.add_cart_button)
        # create a button "Remove from Cart"
        self.remove_cart_button = QPushButton("Remove from Cart", self)
        self.remove_cart_button.move(450, 200)
        layout.addWidget(self.remove_cart_button)

#       create a button "Place Order"
        self.place_order_button = QPushButton("Place Order", self)
        self.place_order_button.move(550, 200)
        layout.addWidget(self.place_order_button)

        # create a button "Order History"
        self.order_his_button = QPushButton("Order History", self)
        self.order_his_button.move(650, 200)
        layout.addWidget(self.order_his_button)
        # create a button "change password"
        self.change_pass_button = QPushButton("Change Password", self)
        self.change_pass_button.move(750, 200)
        layout.addWidget(self.change_pass_button)
        # create a button "Add money to wallet"
        self.add_money_button = QPushButton("Add money to wallet", self)
        self.add_money_button.move(850, 200)
        layout.addWidget(self.add_money_button)
        self.view_profile = QPushButton("View Profile", self)
        self.view_profile.move(950, 200)
        layout.addWidget(self.view_profile)
#         create a button " Delivery Status"
        self.del_st_button = QPushButton("Delivery Status", self)
        self.del_st_button.move(1050, 200)
        layout.addWidget(self.del_st_button)
#         create a button "Back"
        self.back_button = QPushButton("Back", self)
        self.back_button.move(1150, 200)
        layout.addWidget(self.back_button)
#         create a button "Exit"
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.move(1250, 200)
        layout.addWidget(self.exit_button)

    #     button click events:
        self.exit_button.clicked.connect(self.exit_application)

    #     buttons functions:

    def exit_application(self):
        QApplication.quit()




