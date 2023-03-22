import mysql.connector
from mysql.connector import errorcode
#connecting to the database
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
    cursor.execute("Select * from admin where admin_id = %s", (id,))
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
    elif choice == 4:
        customer_menu()
    else:
        print("Invalid choice. Please try again.")
        view_products()
def view_categories():
    cursor.execute("SELECT * FROM CATEGORY")
    res = cursor.fetchall()
    for i in res:
        print("Category ID: " + str(i[0]) + " Category name: " + str(i[1]))
    customer_menu()
def view_cart(id):
    cursor.execute("SELECT * FROM CART WHERE CUSTOMER_ID = %s", (id,))
    res = cursor.fetchall()
    total_price = 0
    total_quantity = 0
    for i in res:
        print("Product ID: " + str(i[1]) + " Product name: " + str(i[2]) + " Product price: " + str(i[3]) + " Product quantity: " + str(i[4]))
        total_price += i[3]*i[4]
        total_quantity += i[4]
    print("Total price: " + str(total_price))
    print("Total quantity: " + str(total_quantity))
    customer_menu(id)

def add_to_cart(id):
    print("Please enter the product ID: ")
    product_id = int(input())
    print("Please enter the quantity: ")
    quantity = int(input())
    cursor.execute("INSERT INTO CART VALUES (%s, %s, %s, %s, %s)", (id, product_id, quantity, 0, 0))
    db.commit()
    
def remove_from_cart(id):
    print("Please enter the product ID: ")
    product_id = int(input())
    cursor.execute("DELETE FROM CART WHERE CUSTOMER_ID = %s AND PRODUCT_ID = %s", (id, product_id))
    db.commit()



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
    print("8. Change wallet balance")
    print("9. Exit")
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
        exit()
    else:
        print("Invalid choice. Please try again.")
        customer_menu()
def delivery_man_menu(id):
    print("Hello! Welcome to the delivery man menu")
    print("Please select an option from the following:")
    print("1. View orders")
    print("2. View customer details")
    print("3. Change password")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
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
    choice = int(input("Enter your choice: "))


starting_menu()
