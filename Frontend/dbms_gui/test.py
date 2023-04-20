# import sys
# import mysql.connector
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
# from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Connect to the MySQL database
#         self.db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
#         # check if the connection is successful
#         if self.db.is_connected():
#             print("Connected to MySQL database")
#         else:
#             print("Connection failed")
#         # Set the table to use
#         self.model.setTable("product")
#         # Select all rows
#         self.model.select()
#         # check if the table is loaded
#         if self.model.lastError().isValid():
#             print("Error loading table: ", self.model.lastError().text())
#             sys.exit(1)
#         else:
#             print("Table loaded successfully")
#
#         self.view = QTableView(self)
#         self.view.setModel(self.model)
#
#         self.setCentralWidget(self.view)
#         self.setWindowTitle("MySQL Table Viewer")
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton
from PyQt5.QtGui import  QStandardItemModel, QStandardItem
import mysql.connector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MySQL Table Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create a database connection
        db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")

        # Create a cursor and execute a SELECT query
        cursor = db.cursor()
        cursor.execute("SELECT * FROM product")

        # Create a standard item model
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Product_ID", "Product_name", "Product_price", "Product_quantity","Category_ID","Admin_ID"])

        # Add the rows to the model using QStandardItem objects
        for row_num, row_data in enumerate(cursor):
            for col_num, col_data in enumerate(row_data):
                item = QStandardItem(str(col_data))
                model.setItem(row_num, col_num, item)

        # Create a view and set its model
        view = QTableView()
        view.setModel(model)
        # create a back button and connect it to the main window's close event
        back_button = QPushButton("Back", self)
        back_button.move(100, 50)
        back_button.clicked.connect(self.close)
        # # Start the main event loop
        # app = QApplication.instance()
        # app.exec_()

        # Add the view to the main window
        self.setCentralWidget(view)

        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
