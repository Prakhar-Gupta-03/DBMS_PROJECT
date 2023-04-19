import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget

class main_menu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.customer_menu_button = QPushButton("Customer Menu")
        self.customer_menu_button.move(50, 200)
        layout.addWidget(self.customer_menu_button)
        self.admin_menu_button = QPushButton("Admin Menu")
        self.admin_menu_button.move(150, 200)
        layout.addWidget(self.admin_menu_button)
        self.delivey_man_button = QPushButton("Delivery Man")
        self.delivey_man_button.move(250, 200)
        layout.addWidget(self.delivey_man_button)
        self.exit_button = QPushButton("Exit")
        self.exit_button.move(350, 200)
        layout.addWidget(self.exit_button)

        #     button click events:
        self.exit_button.clicked.connect(self.exit_application)

    #     buttons functions:
    def exit_application(self):
        QApplication.quit()