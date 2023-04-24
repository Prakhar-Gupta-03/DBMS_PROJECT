import sys

import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget, \
    QLineEdit, QMessageBox
import functions
class add_to_cart(QWidget):
    print("add to cart")
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.tci = take_cus_input()
        self.back_button = QPushButton("Back")
        self.back_button.move(50, 200)
        layout.addWidget(self.back_button)
        self.add_to_cart_button = QPushButton("Add to cart")
        self.add_to_cart_button.clicked.connect(self.save_Details)
        self.add_to_cart_button.move(150, 200)
        layout.addWidget(self.add_to_cart_button)
        self.quantity_label = QLabel("Quantity")
        self.quantity_label.move(50, 200)
        self.quantity_edit = QLineEdit()
        self.quantity_edit.move(150, 200)
        layout.addWidget(self.quantity_edit)
        self.id_label = QLabel("Product ID")
        self.id_label.move(50, 200)
        self.id_edit = QLineEdit()
        self.id_edit.move(150, 200)
        layout.addWidget(self.id_edit)


    def save_Details(self,customer_id):
        print("save details")
        print(customer_id)
        quan = self.quantity_edit.text()
        id = self.id_edit.text()
        print(quan, id)
        if quan == "" or id == "":
            QMessageBox.warning(self, "Error", "Please fill all the fields")
        else:
            print(quan, id)
            functions.add_to_cart_func(self,quan,id,customer_id)
            QMessageBox.information(self, "Success", "Product added to cart successfully")
        # return self.quantity, self.id, customer_id


class take_cus_input(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.customer_id_label = QLabel("Customer ID")
        self.customer_id_label.move(50, 200)
        layout.addWidget(self.customer_id_label)
        self.customer_id = QLineEdit()
        self.customer_id.move(150, 200)
        layout.addWidget(self.customer_id)
        self.customer_id_button = QPushButton("Enter")
        self.customer_id_button.move(250, 200)
        layout.addWidget(self.customer_id_button)
        self.customer_id_button.clicked.connect(self.save_customer_id)
    def save_customer_id(self):
        self.customer_id_save = self.customer_id.text()
        QMessageBox.information(self, "Success", "Customer ID saved successfully")

        # return self.customer_id_save
    def forget_customer_id(self):
        self.customer_id = ""

class place_order(QWidget):
    def __init__(self,customer_id):
        super().__init__()
        layout = QVBoxLayout(self)
        id = customer_id
        db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO ORDERS(customer_id, order_datetime) VALUES (%s, now())", (id,))
            db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return
        else:
            try:
                # find the order_id of the order placed
                cursor.execute(
                    "select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
                res = cursor.fetchall()
                order_id = res[0][0]
                # find the total price of the order placed
                cursor.execute(
                    "select sum(product.product_price*cart.product_quantity) from product, cart where product.product_id = cart.product_id and cart.customer_id = %s",
                    (id,))
                res = cursor.fetchall()
                total_price = res[0][0]
                # update the order_amount in the orders table
                cursor.execute(
                    "update orders set order_amount = %s where order_id = %s", (total_price, order_id))
                db.commit()
            except mysql.connector.Error as err:
                print("Error: {}".format(err))
                return
            else:
                layout.addWidget(QLabel("Order placed successfully"))
        # time.sleep(2)
        print("Processing the order...")
        # adding all the products from the cart to the all_orders table along with the order_id
        cursor.execute(
            "select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
        res = cursor.fetchall()
        order_id = res[0][0]
        cursor.execute(
            "select product_id, product_quantity from cart where customer_id = %s", (id,))
        res = cursor.fetchall()
        for i in res:
            cursor.execute(
                "insert into all_orders(order_id, customer_id, product_id, product_quantity, product_price) values (%s, %s, %s, %s, (select product_price from product where product_id = %s))",
                (order_id, id, i[0], i[1], i[0]))
            db.commit()
        # print the order details
        print("----------------------------------BILL----------------------------------")
        layout.addWidget(QLabel("----------------------------------BILL----------------------------------"))

        print()
        print("Order ID: " + str(order_id))
        layout.addWidget(QLabel("Order ID: " + str(order_id)))
        # print("Order date and time: " + str(datetime.datetime.now()))
        print("Product ID\tProduct quantity\tProduct price\t\tProduct Name")
        layout.addWidget(QLabel("Product ID\tProduct quantity\tProduct price\t\tProduct Name"))
        total_quantity = 0
        cursor.execute(
            "select product_id, product_quantity, product_price from all_orders where customer_id = %s and order_id = %s",
            (id, order_id))
        res = cursor.fetchall()
        for i in res:
            cursor.execute(
                "select product_name from product where product_id = %s", (i[0],))
            res1 = cursor.fetchall()
            print(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" +
                  str(i[2]) + "\t\t\t" + str(res1[0][0]))
            layout.addWidget(QLabel(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" +
                    str(i[2]) + "\t\t\t" + str(res1[0][0])))
            total_quantity += i[1]
        print("Total price: " + str(total_price))
        layout.addWidget(QLabel("Total price: " + str(total_price)))
        print("Total quantity: " + str(total_quantity))
        layout.addWidget(QLabel("Total quantity: " + str(total_quantity)))
        print("------------------------------------------------------------------------")
        layout.addWidget(QLabel("------------------------------------------------------------------------"))
        # updating the product quantity in the product table
        cursor.execute(
            "select product_id, product_quantity from cart where customer_id = %s", (id,))
        res = cursor.fetchall()
        for i in res:
            cursor.execute(
                "update product set product_quantity = product_quantity - %s where product_id = %s", (i[1], i[0]))
            db.commit()
        # removing all the products from the cart
        cursor.execute("DELETE FROM CART WHERE CUSTOMER_ID = %s", (id,))
        # pause execution of the program for 1 seconds
        print("Assigning a delivery man for the order...")
        layout.addWidget(QLabel("Assigning a delivery man for the order..."))
        # time.sleep(2)
        # try:
        # finding the delivery man with the least number of orders
        # getting a count of all the deliveries assigned for each delivery man
        cursor.execute(
            "Select delivery_man.delivery_man_id, count(order_delivery_man.order_ID) as number_of_deliveries from delivery_man left join order_delivery_man on delivery_man.delivery_man_id = order_delivery_man.delivery_man_id group by delivery_man.delivery_man_id order by number_of_deliveries ASC")
        res = cursor.fetchall()
        assigned_delivery_man_id = res[0][0]
        # finding the order_id of the order placed
        cursor.execute(
            "select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
        res = cursor.fetchall()
        order_id = res[0][0]
        # assigning the order with order_id to the delivery_man
        cursor.execute("insert into order_delivery_man(delivery_man_id, order_id, delivery_date) values(%s, %s, now())",
                       (assigned_delivery_man_id, order_id))
        db.commit()
        print("Order is assigned to a delivery man successfully!")
        layout.addWidget(QLabel("Order is assigned to a delivery man successfully!"))



class add_money_to_wallet(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.setWindowTitle("Add money to wallet")
        self.setGeometry(100, 100, 500, 500)
        self.amount_label = QLabel("Enter the amount to be added to the wallet")
        self.amount = QLineEdit()
        self.add_money_button = QPushButton("Add money")
        layout.addWidget(self.add_money_button)
        self.back_button = QPushButton("Back")
        layout.addWidget(self.back_button)
        self.add_money_button.clicked.connect(self.save_details)
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount)

    def save_details(self,customer_id):
        amount = self.amount.text()
        id = customer_id
        if amount == "":
            print("Please enter the amount")
            return
        try:
            functions.add_money_to_wallet_func(id, amount)
            QMessageBox.about(self, "Success", "Money added to wallet successfully")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))

class view_profile(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.setWindowTitle("View Profile")
        self.setGeometry(100, 100, 500, 500)
        db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
        cursor = db.cursor()



