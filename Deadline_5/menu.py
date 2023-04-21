import mysql.connector
from mysql.connector import errorcode
import time
import datetime
# connecting to the database
db = mysql.connector.connect(host="localhost", user="root", passwd="vartika", database="test")
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
        if (id != -1):
            customer_menu(id)
        else:
            starting_menu()
    elif choice == 2:
        id = delivery_man_verification()
        if (id != -1):
            delivery_man_menu(id)
        else:
            starting_menu()
    elif choice == 3:
        id = admin_verification()
        if (id != -1):
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
    id = int(input("Enter your delivery man ID: "))
    cursor.execute("Select * from delivery_man where delivery_man_id = %s", (id,))
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
    print("4. View products in increasing order of price")
    print("5. View products in decreasing order of price")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    # printing the products of the store
    if choice == 1:
        cursor.execute("SELECT * FROM PRODUCT")
        res = cursor.fetchall()
        print("Product_ID\tProduct Price\tProduct Quantity\t\tCategory_ID\t\tProduct Name")
        for i in res:
            print(str(i[0]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[1]))
    # printing the products of a particular category
    elif choice == 2:
        category_id = int(input("Enter category ID: "))
        cursor.execute(
            "SELECT * FROM PRODUCT WHERE CATEGORY_ID = %s", (category_id,))
        res = cursor.fetchall()
        print("Product_ID\tProduct Price\tProduct Quantity\t\tCategory_ID\t\tProduct Name")
        for i in res:
            print(str(i[0]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[1]))
    # printing the products in a particular price range
    elif choice == 3:
        min_price = int(input("Enter minimum price: "))
        max_price = int(input("Enter maximum price: "))
        cursor.execute("SELECT * FROM PRODUCT WHERE PRODUCT_PRICE BETWEEN %s and %s order by PRODUCT_PRICE", (min_price, max_price))
        print("Product_ID\tProduct Price\tProduct Quantity\t\tCategory_ID\t\tProduct Name")
        res = cursor.fetchall()
        for i in res:
            print(str(i[0]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[1]))
    # printing the products in increasing order of price
    elif choice == 4:
        cursor.execute("SELECT * FROM PRODUCT ORDER BY PRODUCT_PRICE")
        res = cursor.fetchall()
        print("Product_ID\tProduct Price\tProduct Quantity\t\tCategory_ID\t\tProduct Name")
        for i in res:
            print(str(i[0]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[1]))
    # printing the products in decreasing order of price
    elif choice == 5:
        cursor.execute("SELECT * FROM PRODUCT ORDER BY PRODUCT_PRICE DESC")
        res = cursor.fetchall()
        print("Product_ID\tProduct Price\tProduct Quantity\t\tCategory_ID\t\tProduct Name")
        for i in res:
            print(str(i[0]) + "\t\t" + str(i[2]) + "\t\t" + str(i[3]) + "\t\t" + str(i[4]) + "\t\t" + str(i[1]))
    # exiting the view products menu
    elif choice == 6:
        return
    # invalid choice
    else:
        print("Invalid choice. Please try again.")
        view_products()


def view_categories():
    cursor.execute("SELECT * FROM CATEGORY")
    res = cursor.fetchall()
    print("Category ID\tCategory Name")
    for i in res:
        print(str(i[0]) + "\t\t" + str(i[1]))


def view_cart(id):
    cursor.execute("SELECT * FROM CART WHERE CUSTOMER_ID = %s", (id,))
    res = cursor.fetchall()
    total_price = 0
    total_quantity = 0
    print("----------------------------CART----------------------------")
    print()
    print()
    print("Product ID\tProduct quantity\tProduct price\t\tCategory ID\t\tProduct name")
    for i in res:
        cursor.execute("SELECT * FROM PRODUCT WHERE PRODUCT_ID = %s", (i[1],))
        product = cursor.fetchall()
        print(str(i[1]) + "\t\t" + str(i[2]) + "\t\t\t" + str(product[0][2]) + "\t\t" + str(product[0][4]) + "\t\t" + str(product[0][1]))
        total_price += product[0][2] * i[2]
        total_quantity += i[2]
    print()
    print("Total price: " + str(total_price))
    print("Total quantity: " + str(total_quantity))
    print()
    print()
    print("----------------------------------------------------------")
    customer_menu(id)


def add_to_cart(id):
    try:
        print("Please enter the product ID: ")
        product_id = int(input())
        print("Please enter the quantity: ")
        quantity = int(input())
        cursor.execute(
            "INSERT INTO CART(customer_id, product_id, product_quantity) VALUES (%s, %s, %s)", (id, product_id, quantity))
        db.commit()
    except ValueError:
        print("Invalid input. Please try again.")
        add_to_cart(id)
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        text_error = err.msg
        if (text_error == "Product already exists in cart"):
            try:
                cursor.execute(
                    "UPDATE CART SET product_quantity = product_quantity + %s WHERE customer_id = %s AND product_id = %s", (quantity, id, product_id))
                db.commit()
            except mysql.connector.Error as err:
                print("Error: {}".format(err))


def remove_from_cart(id):
    try:
        print("Please enter the product ID: ")
        product_id = int(input())
        cursor.execute(
            "DELETE FROM CART WHERE CUSTOMER_ID = %s AND PRODUCT_ID = %s", (id, product_id))
        db.commit()
    except ValueError:
        print("Invalid input. Please try again.")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))


def order_history(id):
    # count the number of orders placed by the customer
    cursor.execute(
        "select count(*) from all_orders where customer_id = %s group by order_id", (id,))
    res = cursor.fetchall()
    print("Number of orders placed: " + str(len(res)))
    # display the order history
    cursor.execute(
        "select order_id from all_orders where customer_id = %s group by order_id", (id,))
    res = cursor.fetchall()
    for i in res:
        print()
        print("-------------------------------------------------------------------")
        print("Order ID: " + str(i[0]))
        cursor.execute(
            "select product_ID, product_quantity, product_price from all_orders where customer_id = %s and order_id = %s", (id, i[0]))
        res1 = cursor.fetchall()
        total_price = 0
        total_quantity = 0
        print("Product_ID\tProduct_quantity\tProduct_price\t\tProduct_Name")
        for j in res1:
            cursor.execute(
                "select product_name from product where product_id = %s", (j[0],))
            res2 = cursor.fetchall()
            print(str(j[0]) + "\t\t\t" + str(j[1]) + "\t\t\t" +
                  str(j[2]) + "\t\t\t" + str(res2[0][0]))
            total_price += j[1]*j[2]
            total_quantity += j[1]
        print()
        print("Total price: " + str(total_price))
        print("Total quantity: " + str(total_quantity))
        print("-------------------------------------------------------------------")


def place_order(id):
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
                "select sum(product.product_price*cart.product_quantity) from product, cart where product.product_id = cart.product_id and cart.customer_id = %s", (id,))
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
            print("Order placed successfully!")
    time.sleep(2)
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
        cursor.execute("insert into all_orders(order_id, customer_id, product_id, product_quantity, product_price) values (%s, %s, %s, %s, (select product_price from product where product_id = %s))",
                       (order_id, id, i[0], i[1], i[0]))
        db.commit()
    # print the order details
    print("----------------------------------BILL----------------------------------")
    print()
    print("Order ID: " + str(order_id))
    print("Order date and time: " + str(datetime.datetime.now()))
    print("Product ID\tProduct quantity\tProduct price\t\tProduct Name")
    total_quantity = 0
    cursor.execute(
        "select product_id, product_quantity, product_price from all_orders where customer_id = %s and order_id = %s", (id, order_id))
    res = cursor.fetchall()
    for i in res:
        cursor.execute(
            "select product_name from product where product_id = %s", (i[0],))
        res1 = cursor.fetchall()
        print(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" +
              str(i[2]) + "\t\t\t" + str(res1[0][0]))
        total_quantity += i[1]
    print("Total price: " + str(total_price))
    print("Total quantity: " + str(total_quantity))
    print("------------------------------------------------------------------------")
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
    time.sleep(2)
    try:
        # finding the delivery man with the least number of orders
        # getting a count of all the deliveries assigned for each delivery man
        cursor.execute("Select delivery_man.delivery_man_id, count(order_delivery_man.order_ID) as number_of_deliveries from delivery_man left join order_delivery_man on delivery_man.delivery_man_id = order_delivery_man.delivery_man_id group by delivery_man.delivery_man_id order by number_of_deliveries ASC")
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
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return

 
def change_password(id):
    try: 
        password = input("Enter new password: ")
        cursor.execute("update customer set customer_password=%s where customer_id=%s", (password, id))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return


def change_wallet_balance(id):
    try: 
        wallet_add = input("Enter the amount to be added to the wallet: ")
        cursor.execute("update customer set customer_wallet=customer_wallet+" + wallet_add + " where customer_id=" + str(id))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return

 
def delivery_man_details(id):
    # finding the order_ids placed by the customer
    cursor.execute("select order_id from orders where customer_id = %s", (id,))
    res = cursor.fetchall()
    print("Order_ID\t\tDelivery_Man_ID\t\tDelivery_Date\t\tDelivery_contact_number\t\tDelivery_Man_Name")
    for i in res:
        # for each order_id, fetch the delivery_man_id from order_delivery_man
        current_order_id = i[0]
        cursor.execute("select delivery_man_id, delivery_date from order_delivery_man where order_id = %s", (current_order_id,))
        res1 = cursor.fetchall()
        delivery_man_id = res1[0][0]
        delivery_date = res1[0][1]
        # fetching the details of the delivery_man from the delivery_man table
        cursor.execute("select delivery_man_id, man_name, man_contact from delivery_man where delivery_man_id = %s", (delivery_man_id,))
        res2 = cursor.fetchall()
        print(str(current_order_id) + "\t\t\t" + str(res2[0][0]) + "\t\t\t" + str(delivery_date) + "\t\t\t" + str(res2[0][2]) + "\t\t\t" + str(res2[0][1]))
    return


def view_profile_customer(id):
    cursor.execute("select * from customer where customer_id = %s", (id,))
    res = cursor.fetchall()
    print("Customer ID: " + str(id))
    print("Customer First Name: " + res[0][0])
    print("Customer Last Name: " + res[0][1])
    print("Customer Email: " + res[0][2])
    print("Customer Password: " + res[0][3])
    print("Customer Wallet Balance: " + str(res[0][4]))
    print("Customer Address: " + str(res[0][5]) + ", " + res[0][6] + ", " + res[0][7] + ", " + res[0][8] + ", " + res[0][9])
    print("Customer Contact Number: " + res[0][10])


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
    print("11. View profile")
    print("12. Exit")
    print("13. Go Back")
    try: 
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please try again.")
        customer_menu(id)
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
        view_profile_customer(id)
    elif choice == 12: 
        exit()
    elif choice == 13:
        starting_menu()
    else:
        print("Invalid choice. Please try again.")
        customer_menu(id)
    customer_menu(id)


def view_orders_to_be_delivered(id):
    cursor.execute(
        "select order_id from order_delivery_man where delivery_man_id = %s", (id,))
    res = cursor.fetchall()
    print("Order ID\tCustomer ID\tOrder Date\tTotal Price\tTotal Quantity")
    for i in res:
        # fetch the order details for each order_id
        cursor.execute("select * from orders where order_id = %s", (i[0],))
        res1 = cursor.fetchall()
        # compute the total price of the order
        cursor.execute("select product_price, product_quantity from all_orders where order_id = %s", (i[0],))
        res2 = cursor.fetchall()
        total_price = 0
        total_quantity = 0
        for j in res2:
            total_price += j[0] * j[1]
            total_quantity += j[1]
        print(str(res1[0][0]) + "\t\t" + str(res1[0][1]) + "\t\t" + str(res1[0][2]) + "\t\t" + str(total_price) + "\t\t" + str(total_quantity))


def view_customer_details_for_order(id):
    try: 
        order_id = int(input("Enter the order ID for which you want to view the customer details: "))
    except ValueError:
        print("Invalid order ID. Please try again.")
        view_customer_details_for_order(id)
    else:
        # check whether the order_id has a relation with the delivery man
        cursor.execute("select * from order_delivery_man where order_id = %s and delivery_man_id = %s", (order_id, id))
        res = cursor.fetchall()
        if (len(res) == 0):
            print("Invalid order ID. Please try again.")
            view_customer_details_for_order(id)
        else:
            cursor.execute(
                "select customer_id from orders where order_id = %s", (order_id,))
            res = cursor.fetchall()
            customer_id = res[0][0]
            cursor.execute("select customer_fname, customer_lname, customer_contact_number, customer_address_buildingno, customer_address_street, customer_address_city, customer_address_state, customer_address_pincode from customer where customer_id = %s", (customer_id,))
            res = cursor.fetchall()
            print("Customer first name: " + str(res[0][0]))
            print("Customer last name: " + str(res[0][1]))
            print("Customer contact number: " + str(res[0][2]))
            print("Customer Address: " + str(res[0][3]) + ", " + res[0][4] + ", " + res[0][5] + ", " + res[0][6])
            print("Customer Pincode: " + str(res[0][7]))


def change_delivery_man_password(id):
    try: 
        password = input("Enter new password: ")
        cursor.execute("update delivery_man set man_pass = %s where delivery_man_id = %s", (password, id))
        db.commit()
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        db.rollback()
    else:
        print("Password changed successfully")
        

def view_profile(id):
    try: 
        cursor.execute("select * from delivery_man where delivery_man_id = %s", (id,))
        res = cursor.fetchall()
        print("Delivery Man ID: " + str(res[0][0]))
        print("Delivery Man Name: " + str(res[0][1]))
        print("Delivery Man Contact Number: " + str(res[0][2]))
        print("Delivery Man Email ID: " + str(res[0][3]))
        cursor.execute("Select count(*) from order_delivery_man where delivery_man_id = %s", (id,))
        res = cursor.fetchall()
        print("Number of orders assigned to be delivered: " + str(res[0][0]))
    except mysql.connector.Error as error:
        print("There was an error while fetching the data from the database: {}".format(error))


def delivery_man_menu(id):
    print("Hello! Welcome to the delivery man menu")
    print("Please select an option from the following:")
    print("1. View orders")
    print("2. View customer details")
    print("3. Change password")
    print("4. View Profile")
    print("5. Exit")
    print("6. Go Back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_orders_to_be_delivered(id)
    elif choice == 2:
        view_customer_details_for_order(id)
    elif choice == 3:
        change_delivery_man_password(id)
    elif choice == 4:
        view_profile(id)
    elif choice == 5:
        exit()
    elif choice == 6:
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
        cursor.execute("insert into product (product_name, product_price, product_quantity, Category_ID, Admin_ID) values (%s, %s, %s, %s, %s)",
                       (product_name, product_price, product_quantity, Category_ID, Admin_ID,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def add_category(id):
    Admin_ID = id
    category_name = input("Enter category name: ")
    try:
        cursor.execute(
            "insert into category (category_name,Admin_ID) values (%s, %s)", (category_name, Admin_ID,))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def remove_product():
    product_id = int(input("Enter product ID: "))
    # check if product exists
    cursor.execute(
        "select product_id from product where product_id = %s", (product_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Product does not exist")
    else:
        # remove the product from the cart
        cursor.execute("delete from cart where product_id = %s", (product_id,))
        cursor.execute(
            "delete from all_orders where product_id = %s", (product_id,))
        cursor.execute(
            "delete from product where product_id = %s", (product_id,))
        db.commit()


def remove_category():
    category_id = input("Enter category id: ")
    # check if category exists
    cursor.execute(
        "select category_id from category where category_id = %s", (category_id,))
    res = cursor.fetchall()
    if len(res) == 0:
        print("Error: Category does not exist")
    else:
        # remove all the products in the category
        cursor.execute(
            "select product_id from product where Category_ID = %s", (res[0][0],))
        res = cursor.fetchall()
        for i in res:
            # remove the products from the cart
            cursor.execute("delete from cart where product_id = %s", (i[0],))
            cursor.execute(
                "delete from all_orders where product_id = %s", (i[0],))
            cursor.execute(
                "delete from product where product_id = %s", (i[0],))
        # remove the category
        cursor.execute(
            "delete from category where category_id = %s", (category_id,))
        db.commit()


def change_product_price():
    product_id = int(input("Enter product ID: "))
    product_price = int(input("Enter new product price: "))
    if (product_price < 0):
        print("Invalid price. Please try again.")
    else:
        try:
            cursor.execute(
                "update product set product_price = %s where product_id = %s", (product_price, product_id))
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
            cursor.execute(
                "update product set product_quantity = %s where product_id = %s", (product_quantity, product_id))
            db.commit()
        except mysql.connector.Error as err:
            print("Error: {}".format(err.msg))


def change_admin_password(id):
    password = input("Enter new password: ")
    try:
        cursor.execute(
            "update admin_shop set admin_password = %s where admin_id = %s", (password, id))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def total_sales_for_each_product(id):
    try:
        cursor.execute("select product.product_name, sum(all_orders.product_quantity) from all_orders join product where product.product_ID = all_orders.product_ID group by product.product_ID order by sum(all_orders.product_quantity) desc")
        res = cursor.fetchall()
        print("Total sales for each product: ")
        print("Total Sales\t\t\tProduct Name")
        for i in res:
            print(i[1], "\t\t\t\t", i[0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def total_sales_for_each_category(id):
    try: 
        cursor.execute("select category.category_name, sum(all_orders.product_quantity) from all_orders join product join category where product.product_ID = all_orders.product_ID and product.Category_ID = category.category_ID group by category.category_ID order by sum(all_orders.product_quantity) desc")
        res = cursor.fetchall()
        print("Total sales for each category: ")
        print("Total Sales\t\t\tCategory Name")
        for i in res:
            print(i[1], "\t\t\t\t", i[0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def arranging_customers_by_total_amount_spent(id):
    try: 
        cursor.execute("select customer.customer_fname, sum(all_orders.product_quantity * product.product_price) from all_orders join product join customer where product.product_ID = all_orders.product_ID and all_orders.customer_ID = customer.customer_ID group by customer.customer_ID order by sum(all_orders.product_quantity * product.product_price) desc")
        res = cursor.fetchall()
        print("Arranging the customers by the total amount spent: ")
        print("Total Amount Spent\t\t\tCustomer Name")
        for i in res:
            print(i[1], "\t\t\t\t", i[0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def customer_retention_rate(id):
    try: 
        cursor.execute("select customer.customer_fname, count(all_orders.order_ID) from all_orders join customer where all_orders.customer_ID = customer.customer_ID group by customer.customer_ID order by count(all_orders.order_ID) desc")
        res = cursor.fetchall()
        # count number of customers with more than 1 order
        count = 0
        for i in res:
            if i[1] > 1:
                count += 1
        print("Number of customers with more than 1 order: ", count)
        print("Total number of unique customers: ", len(res))
        print("Customer retention rate: ", count/len(res)*100, "%")
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def average_amount_spent_by_customer(id):
    try: 
        cursor.execute("select customer.customer_fname, sum(all_orders.product_quantity * product.product_price) from all_orders join product join customer where product.product_ID = all_orders.product_ID and all_orders.customer_ID = customer.customer_ID group by customer.customer_ID order by sum(all_orders.product_quantity * product.product_price) desc")
        res = cursor.fetchall()
        # find the total amount spent by all customers
        total = 0
        for i in res:
            total += i[1]
        print("Total amount spent by all customers: ", total)
        # find the total number of unique orders
        cursor.execute("select count(distinct order_ID) from all_orders")
        res = cursor.fetchall()
        print("Total number of unique orders: ", res[0][0])
        print("Average amount spent by the customer: ", total/res[0][0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def total_revenue_by_month(id):
    try: 
        cursor.execute("select monthname(orders.order_datetime), sum(all_orders.product_quantity * product.product_price) from all_orders join product join orders where product.product_ID = all_orders.product_ID and all_orders.order_ID = orders.order_ID group by monthname(orders.order_datetime) order by monthname(orders.order_datetime)")
        res = cursor.fetchall()
        print("Total revenue by the month: ")
        print("Month\t\t\tTotal Revenue")
        for i in res:
            print(i[0], "\t\t\t\t", i[1])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def total_number_of_products_sold_by_month(id):
    try: 
        cursor.execute("select monthname(orders.order_datetime), sum(all_orders.product_quantity) from all_orders join orders where all_orders.order_ID = orders.order_ID group by monthname(orders.order_datetime) order by monthname(orders.order_datetime)")
        res = cursor.fetchall()
        print("Total number of products sold by the month: ")
        print("Month\t\t\tTotal Number of Products Sold")
        for i in res:
            print(i[0], "\t\t\t\t", i[1])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def total_revenue_by_month_and_category(id):
    try: 
        cursor.execute("select monthname(orders.order_datetime), category.category_name, sum(all_orders.product_quantity * product.product_price) from all_orders join product join orders join category where product.product_ID = all_orders.product_ID and all_orders.order_ID = orders.order_ID and product.Category_ID = category.category_ID group by monthname(orders.order_datetime), category.category_name order by monthname(orders.order_datetime), category.category_name")
        res = cursor.fetchall()
        print("Total revenue by the month and the category: ")
        print("Month\t\t\tTotal Revenue\t\t\tCategory Name")
        for i in res:
            print(i[0], "\t\t\t\t", i[2], "\t\t\t\t", i[1])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def revenue_by_customer_location(id):
    try: 
        cursor.execute("select customer.customer_address_city, sum(all_orders.product_quantity * product.product_price) from all_orders join product join customer where product.product_ID = all_orders.product_ID and all_orders.customer_ID = customer.customer_ID group by customer.customer_address_city order by sum(all_orders.product_quantity * product.product_price) desc")
        res = cursor.fetchall()
        print("Revenue by the customer location: ")
        print("Total Revenue\t\t\tCustomer City")
        for i in res:
            print(i[1], "\t\t\t\t", i[0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def top_selling_product_by_category(id):
    try: 
        cursor.execute("select category.category_name, product.product_name, sum(all_orders.product_quantity) from all_orders join product join category where product.product_ID = all_orders.product_ID and product.Category_ID = category.category_ID group by product.product_ID order by category.category_name, sum(all_orders.product_quantity) desc")
        res = cursor.fetchall()
        print("Top selling products by category: ")
        print("Total Number of Products Sold\t\t\tProduct Name\t\t\tCategory Name")
        for i in res:
            print(i[2], "\t\t\t\t", i[1], "\t\t\t\t", i[0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def aggregate_sales_by_category_and_date(id):
    try: 
        cursor.execute("select category.category_name, monthname(orders.order_datetime), sum(all_orders.product_quantity * product.product_price) from all_orders join product join orders join category where product.product_ID = all_orders.product_ID and all_orders.order_ID = orders.order_ID and product.Category_ID = category.category_ID group by category.category_name, monthname(orders.order_datetime) order by category.category_name, monthname(orders.order_datetime)")
        res = cursor.fetchall()
        print("Aggregate sales by category and date, and the total sales amount for each category and month: ")
        print("Month\t\t\tTotal Revenue\t\t\tCategory Name")
        for i in res:
            print(i[1], "\t\t\t\t", i[2], "\t\t\t\t", i[0])
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))


def data_statistics(id):
    print("Welcome to the data statistics menu")
    print("Please select an option from the following:")
    print("1. Aggregate sales by category and date, and the total sales amount for each category and month")
    print("2. Top selling products by category")
    print("3. Revenue by the customer location")
    print("4. Total revenue by the month and the category")
    print("5. Average amount spent by the customer")
    print("6. Total number of products sold by the month")
    print("7. Total revenue by the month")
    print("8. Total sales for each product")
    print("9. Total sales for each category")
    print("10. Arranging the customers by the total amount spent")
    print("11. Customer retention rate")
    print("12. Exit")
    print("13. Go Back")
    try: 
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please try again.")
        data_statistics(id)
    if choice == 1:
        aggregate_sales_by_category_and_date(id)
    elif choice == 2:
        top_selling_product_by_category(id)
    elif choice == 3:
        revenue_by_customer_location(id)
    elif choice == 4:
        total_revenue_by_month_and_category(id)
    elif choice == 5:
        average_amount_spent_by_customer(id)
    elif choice == 6:
        total_number_of_products_sold_by_month(id)
    elif choice == 7:
        total_revenue_by_month(id)
    elif choice == 8:
        total_sales_for_each_product(id)
    elif choice == 9:
        total_sales_for_each_category(id)
    elif choice == 10:
        arranging_customers_by_total_amount_spent(id)
    elif choice == 11:
        customer_retention_rate(id)
    elif choice == 12:
        exit()
    elif choice == 13:
        admin_menu(id)
    else:
        print("Invalid input. Please try again.")
        data_statistics(id)
    data_statistics(id)
        

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
    print("10. Data Statistics")
    print("11. Exit")
    print("12. Go Back")
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
        data_statistics(id)
    elif choice == 11:
        exit()
    elif choice == 12:
        starting_menu()
    else:
        print("Invalid choice. Please try again.")
        admin_menu(id)
    admin_menu(id)


starting_menu()
