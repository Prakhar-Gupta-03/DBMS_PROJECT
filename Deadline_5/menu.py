import mysql.connector
from mysql.connector import errorcode
import time
#connecting to the database
# db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
db = mysql.connector.connect(host="localhost", user="prakhar", passwd="prakhar", database="test")
cursor = db.cursor()
def starting_menu():
    print("Hello! Welcome to the retail store database management system.")
    print("Please select an option from the following:")
    print("1. Customer")
    print("2. Delivery Man")
    print("3. Admin")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = customer_verification()
        if (id!=-1):
            customer_menu(id)
        else:
            starting_menu()
    elif choice == 2:
        id = delivery_man_verification()    
        if (id!=-1):
            delivery_man_menu(id)
        else:
            starting_menu()
    elif choice == 3:
        id = admin_verification()
        if (id!=-1):   
            admin_menu(id)
        else:
            starting_menu()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice. Please try again.")
        starting_menu()
    starting_menu()
def customer_verification():
    print("Please enter your customer ID: ")
    id = int(input())
    cursor.execute("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = %s", (id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Invalid customer ID. Please try again.")
        return -1
    else:
        return id
def delivery_man_verification():
    print("Please enter your delivery ID:")
    id = int(input())
    cursor.execute("Select * from delivery_man where delivery_id = %s", (id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Invalid delivery ID. Please try again.")
        return -1
    else:
        return id
def admin_verification():
    print("please enter your admin ID:")
    id = int(input())
    cursor.execute("Select * from admin_shop where admin_id = %s", (id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Invalid admin ID. Please try again.")
        return -1
    else:
        return id
def view_products():
    print("Please select an option from the following: ")
    print("1. View all products")
    print("2. View products by category")
    print("3. View products by price range")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cursor.execute("SELECT * FROM PRODUCT")
        res = cursor.fetchall()
        for i in res:
            print("Product ID: " + str(i[0]) + " Product name: " + str(i[1]) + " Product price: " + str(i[2]) + " Product quantity: " + str(i[3]))
    elif choice == 2:
        category_id = int(input("Enter category ID: "))
        cursor.execute("SELECT * FROM PRODUCT WHERE CATEGORY_ID = %s", (category_id,))
        res = cursor.fetchall()
        for i in res:
            print("Product ID: " + str(i[0]) + " Product name: " + str(i[1]) + " Product price: " + str(i[2]) + " Product quantity: " + str(i[3]))
    elif choice == 3:
        min_price = int(input("Enter minimum price: "))
        max_price = int(input("Enter maximum price: "))
        cursor.execute("SELECT * FROM PRODUCT WHERE PRODUCT_PRICE BETWEEN %s AND %s", (min_price, max_price))
        res = cursor.fetchall()
        for i in res:
            print("Product ID: " + str(i[0]) + " Product name: " + str(i[1]) + " Product price: " + str(i[2]) + " Product quantity: " + str(i[3]))
    else:
        print("Invalid choice. Please try again.")
        view_products()
def view_categories():
    cursor.execute("SELECT * FROM CATEGORY")
    res = cursor.fetchall()
    for i in res:
        print("Category ID: " + str(i[1]) + " Category name: " + str(i[2]))
def view_cart(id):
    cursor.execute("SELECT * FROM CART WHERE CUSTOMER_ID = %s", (id,))
    res = cursor.fetchall()
    total_price = 0
    total_quantity = 0
    for i in res:
        print("Product ID: " + str(i[1]) + " Product quantity: " + str(i[2]))
        cursor.execute("SELECT PRODUCT_PRICE FROM PRODUCT WHERE PRODUCT_ID = %s", (i[1],))
        res1 = cursor.fetchall()
        total_price += res1[0][0]*i[2]
        total_quantity += i[2]
    print("Total price: " + str(total_price))
    print("Total quantity: " + str(total_quantity))
    customer_menu(id)
def add_to_cart(id):
    try:
        print("Please enter the product ID: ")
        product_id = int(input())
        print("Please enter the quantity: ")
        quantity = int(input())
        cursor.execute("INSERT INTO CART(customer_id, product_id, product_quantity) VALUES (%s, %s, %s)", (id, product_id, quantity))
        db.commit()
    except ValueError:
        print("Invalid input. Please try again.")
        add_to_cart(id)
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        text_error = err.msg
        if (text_error=="Product already exists in cart"):
            try: 
                cursor.execute("UPDATE CART SET product_quantity = product_quantity + %s WHERE customer_id = %s AND product_id = %s", (quantity, id, product_id))
                db.commit()
            except mysql.connector.Error as err:
                print("Error: {}".format(err))
def remove_from_cart(id):
    try:
        print("Please enter the product ID: ")
        product_id = int(input())
        cursor.execute("DELETE FROM CART WHERE CUSTOMER_ID = %s AND PRODUCT_ID = %s", (id, product_id))
        db.commit()
    except ValueError:
        print("Invalid input. Please try again.")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
def order_history(id):
    #count the number of orders placed by the customer
    cursor.execute("select count(*) from all_orders where customer_id = %s group by order_id", (id,))
    res = cursor.fetchall()
    print("Number of orders placed: " + str(len(res)))
    #display the order history
    cursor.execute("select order_id from all_orders where customer_id = %s group by order_id", (id,))
    res = cursor.fetchall()
    for i in res:
        print("Order ID: " + str(i[0]))
        cursor.execute("select product_quantity, product_price from all_orders where order_id = %s and customer_id = %s", (i[0], id))
        res1 = cursor.fetchall()
        total_price = 0
        total_quantity = 0
        for j in res1:
            print("Product quantity: " + str(j[0]) + " Product price: " + str(j[1]))
            total_price += j[0]*j[1]
            total_quantity += j[0]
        print("Total price: " + str(total_price))
        print("Total quantity: " + str(total_quantity))
def place_order(id):
    try:
        cursor.execute("INSERT INTO ORDERS(customer_id, order_datetime) VALUES (%s, now())", (id,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return
    else:
        try:
            # find the order_id of the order placed
            cursor.execute("select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
            res = cursor.fetchall()
            order_id = res[0][0]
            # find the total price of the order placed
            cursor.execute("select sum(product_price * product_quantity) from product where product_id in (select product_id from cart where customer_id = %s)", (id,))
            res = cursor.fetchall()
            total_price = res[0][0]
            # update the order_amount in the orders table
            cursor.execute("update orders set order_amount = %s where order_id = %s", (total_price, order_id))
            db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return
        else:
            print("Order placed successfully!")
    time.sleep(2)
    print("Processing the order...")
    # adding all the products from the cart to the all_orders table along with the order_id
    cursor.execute("select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
    res = cursor.fetchall()
    order_id = res[0][0]
    cursor.execute("select product_id, product_quantity from cart where customer_id = %s", (id,))
    res = cursor.fetchall()
    for i in res:
        cursor.execute("insert into all_orders(order_id, customer_id, product_id, product_quantity, product_price) values (%s, %s, %s, %s, (select product_price from product where product_id = %s))", (order_id, id, i[0], i[1], i[0]))
        db.commit()
     # removing all the products from the cart
    cursor.execute("DELETE FROM CART WHERE CUSTOMER_ID = %s", (id,))
    # pause execution of the program for 1 seconds
    print("Assigning a delivery man for the order...")
    time.sleep(2)
    try:
        # finding the delivery man with the least number of orders
        cursor.execute("select delivery_man_id from order_delivery_man group by delivery_man_id order by count(*) ASC LIMIT 1")
        res = cursor.fetchall()
        if (len(res) == 0):
            delivery_id = 1
        else:
            delivery_id = res[0][0]
        # finding the order_id of the order placed
        cursor.execute("select order_id from orders where customer_id = %s order by order_id desc limit 1", (id,))
        res = cursor.fetchall()
        order_id = res[0][0]
        # assigning the order with order_id to the delivery_man
        cursor.execute("insert into order_delivery_man(delivery_man_id, order_id, delivery_date) values (%s, %s, now())", (delivery_id, order_id))
        db.commit()
        print("Order is assigned to a delivery man successfully!")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return

def change_password(id):
    password = input("Enter new password: ")
    cursor.execute("update customer set customer_password=" + password + " where customer_id=" + id)
    db.commit()
def change_wallet_balance(id):
    wallet_balance = int(input("Enter new wallet balance: "))
    cursor.execute("update customer set wallet_balance=" + wallet_balance + " where customer_id=" + id)
    db.commit()
def delivery_man_details(id):
    # check whether the customer has placed an order
    cursor.execute("select count(*) from orders where customer_id = %s", (id,))
    res = cursor.fetchall()
    if res[0][0] == 0:
        print("You have not placed any orders yet.")
    else:
        #fetch the details of the delivery man for the respective order and customer ID
        cursor.execute("select order_id from orders where customer_id = %s", (id,))
        res = cursor.fetchall()
        customer_order_id = res[0][0]
        cursor.execute("select delivery_man_id from order_delivery_man where order_id = %s", (customer_order_id,))
        res = cursor.fetchall()
        delivery_man_id = res[0][0]
        cursor.execute("select man_name, man_contact, man_email, man_pass from delivery_man where delivery_man_id = %s", (delivery_man_id,))
def customer_menu(id):
    print("Hello! Welcome to the customer menu.")
    print("Please select an option from the following:")
    print("1. View products")
    print("2. View categories")
    print("3. View cart")
    print("4. Add to cart")
    print("5. Remove from cart")
    print("6. Place order")
    print("7. Change password")
    print("8. Add wallet balance")
    print("9. Order history")
    print("10. Check the details of the assigned delivery man")
    print("11. Exit")
    print("12. Go Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_products()
    elif choice == 2:
        view_categories()
    elif choice == 3:  
        view_cart(id)
    elif choice == 4:
        add_to_cart(id)
    elif choice == 5:
        remove_from_cart(id)
    elif choice == 6:
        place_order(id)
    elif choice == 7:
        change_password(id)
    elif choice == 8:
        change_wallet_balance(id)
    elif choice == 9:
        order_history(id)
    elif choice == 10:
        delivery_man_details(id)
    elif choice == 11:
        exit()
    elif choice == 12:
        starting_menu()
    else:
        print("Invalid choice. Please try again.")
        customer_menu(id)
    customer_menu(id)
def view_orders_to_be_delivered(id):
    cursor.execute("select order_id from order_delivery_man where delivery_man_id = %s", (id,))
    res = cursor.fetchall()
    for i in res:
        cursor.execute("select order_id, order_datetime, order_amount, customer_id from orders where order_id = %s", (i[0],))
        res1 = cursor.fetchall()
        print("Order ID: " + str(res1[0][0]))
        print("Order date and time: " + str(res1[0][1]))
        print("Order amount: " + str(res1[0][2]))
        print("Customer ID: " + str(res1[0][3]))
def view_customer_details_for_order(id):
    print("Enter the order ID for which you want to view the customer details: ")
    order_id = int(input())
    cursor.execute("select customer_id from orders where order_id = %s", (order_id,))
    res = cursor.fetchall()
    customer_id = res[0][0]
    cursor.execute("select customer_fname, customer_lname, customer_contact_number, customer_address_buildingno, customer_address_street, customer_address_city, customer_address_state, customer_address_pincode from customer where customer_id = %s", (customer_id,))
    res = cursor.fetchall()
    print("Customer first name: " + str(res[0][0]))
    print("Customer last name: " + str(res[0][1]))
    print("Customer contact number: " + str(res[0][2]))
    print("Customer address building number: " + str(res[0][3]))
    print("Customer address street: " + str(res[0][4]))
    print("Customer address city: " + str(res[0][5]))
    print("Customer address state: " + str(res[0][6]))
    print("Customer address pincode: " + str(res[0][7]))
def change_delivery_man_password(id):
    password = input("Enter new password: ")
    cursor.execute("update delivery_man set man_pass = %s where delivery_man_id = %s", (password, id))
    db.commit()
def delivery_man_menu(id):
    print("Hello! Welcome to the delivery man menu")
    print("Please select an option from the following:")
    print("1. View orders")
    print("2. View customer details")
    print("3. Change password")
    print("4. Exit")
    print("5. Go Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_orders_to_be_delivered(id)
    elif choice == 2:
        view_customer_details_for_order(id)
    elif choice == 3:
        change_delivery_man_password(id)
    elif choice == 4:   
        exit()
    elif choice == 5:
        starting_menu()
    else:
        print("Invalid choice. Please try again.")
        delivery_man_menu(id)
    delivery_man_menu(id)
def add_product(id):
    Admin_ID = id
    product_name = input("Enter product name: ")
    product_price = int(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    Category_ID = input("Enter product category: ")
    try: 
        cursor.execute("insert into product (product_name, product_price, product_quantity, Category_ID, Admin_ID) values (%s, %s, %s, %s, %s)", (product_name, product_price, product_quantity, Category_ID, Admin_ID,))
        db.commit()
    except mysql.connector.Error as err: 
        print("Error: {}".format(err.msg))
def add_category(id):
    Admin_ID = id
    category_name = input("Enter category name: ")
    try:
        cursor.execute("insert into category (category_name,Admin_ID) values (%s, %s)", (category_name,Admin_ID,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))
def remove_product():
    product_id = int(input("Enter product ID: "))
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
def remove_category():
    category_name = input("Enter category name: ")
    # check if category exists
    cursor.execute("select category_id from category where category_name = %s", (category_name,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Category does not exist")
    else:
        # remove all the products in the category
        cursor.execute("select product_id from product where Category_ID = %s", (res[0][0],))
        res = cursor.fetchall()
        for i in res:
            # remove the products from the cart
            cursor.execute("delete from cart where product_id = %s", (i[0],))
            cursor.execute("delete from all_orders where product_id = %s", (i[0],))
            cursor.execute("delete from product where product_id = %s", (i[0],))
        # remove the category
        cursor.execute("delete from category where category_name = %s", (category_name,))
        db.commit()
def change_product_price():
    product_id = int(input("Enter product ID: "))
    product_price = int(input("Enter new product price: "))
    if (product_price < 0):
        print("Invalid price. Please try again.")
    else:
        try:
            cursor.execute("update product set product_price = %s where product_id = %s", (product_price, product_id))
            db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err.msg))
def change_product_quantity():
    product_id = int(input("Enter product ID: "))
    product_quantity = int(input("Enter new product quantity: "))
    if (product_quantity < 0):
        print("Invalid quantity. Please try again.")
    else:
        try:
            cursor.execute("update product set product_quantity = %s where product_id = %s", (product_quantity, product_id))
            db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err.msg))
def change_admin_password(id):
    password = input("Enter new password: ")
    try:
        cursor.execute("update admin_shop set admin_password = %s where admin_id = %s", (password, id))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))
def admin_menu(id):
    print("Hello! Welcome to the admin menu")
    print("Please select an option from the following:")
    print("1. View products")
    print("2. View categories")
    print("3. Add product")
    print("4. Add category")
    print("5. Remove product")
    print("6. Remove category")
    print("7. Change product price")
    print("8. Change product quantity")
    print("9. Change password")
    print("10. Exit")
    print("11. Go Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_products()
    elif choice == 2:
        view_categories()
    elif choice == 3:
        add_product(id)
    elif choice == 4:
        add_category(id)
    elif choice == 5:
        remove_product()
    elif choice == 6:
        remove_category()
    elif choice == 7:
        change_product_price()
    elif choice == 8:
        change_product_quantity()
    elif choice == 9:
        change_admin_password(id)
    elif choice == 10:
        exit()
    elif choice == 11:
        starting_menu()
    else:
        print("Invalid choice. Please try again.")
        admin_menu(id)   
    admin_menu(id)
starting_menu()
