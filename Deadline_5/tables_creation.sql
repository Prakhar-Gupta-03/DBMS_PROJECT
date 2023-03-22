USE test;

DROP TABLE IF EXISTS DELIVERY_MAN;
DROP TABLE IF EXISTS CART;
DROP TABLE IF EXISTS ORDERS;
DROP TABLE IF EXISTS PRODUCT;
DROP TABLE IF EXISTS CUSTOMER;
DROP TABLE IF EXISTS CATEGORY;
DROP TABLE IF EXISTS ADMIN_SHOP;

CREATE Table admin_shop(
    Admin_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ADMIN_NAME VARCHAR(50) NOT NULL,
    Admin_Password VARCHAR(50) NOT NULL
);

CREATE Table customer(
    customer_fname VARCHAR(50) NOT NULL,
    customer_lname VARCHAR(50) NOT NULL,
    customer_email VARCHAR(50) NOT NULL,
    customer_password VARCHAR(50) NOT NULL,
    customer_wallet INT Default 0,
    Customer_Address_BuildingNo int NOT NULL,
    Customer_Address_Street VARCHAR(50) NOT NULL,
    Customer_Address_City VARCHAR(50) NOT NULL,
    Customer_Address_State VARCHAR(50) NOT NULL,
    Customer_Address_Pincode VARCHAR(10) NOT NULL DEFAULT 0,
    Customer_Contact_Number VARCHAR(15) NOT NULL,
    Customer_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE Table category(
    Admin_ID INT NOT NULL,
    Foreign Key (Admin_ID) REFERENCES admin_shop(Admin_ID),

    Category_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Category_Name VARCHAR(50) NOT NULL
);

CREATE TABLE product(
    Product_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    product_price INT NOT NULL,
    product_quantity INT NOT NULL,
    Category_ID INT NOT NULL,
    Admin_ID INT NOT NULL,
    Foreign Key (Admin_ID) REFERENCES admin_shop(Admin_ID),
    Foreign Key (Category_ID) REFERENCES category(Category_ID)       
);


CREATE TABLE orders(
    Order_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Foreign Key (Customer_ID) REFERENCES customer(Customer_ID),
    order_DateTime DATETIME NOT NULL,
    order_amount INT NOT NULL DEFAULT 0,
    Admin_ID INT NOT NULL,
    Foreign Key (Admin_ID) REFERENCES admin_shop(Admin_ID)
);

-- the cart table maintains the relation between the customer and the product he has added to his cart
CREATE TABLE cart(
    Customer_ID INT NOT NULL,
    Foreign Key (Customer_ID) REFERENCES customer(Customer_ID),
    Product_ID INT NOT NULL,
    Foreign Key (Product_ID) REFERENCES product(Product_ID),
    product_quantity INT NOT NULL,
    PRIMARY KEY (Customer_ID, Product_ID)
);

-- table only contains the personal details of the delivery man
CREATE Table delivery_man(
    delivery_man_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    man_name VARCHAR(50) NOT NULL,
    man_contact VARCHAR(15) NOT NULL,
    man_email VARCHAR(50) NOT NULL,
    man_pass VARCHAR(20) NOT NULL,
    Admin_ID INT NOT NULL,
    Foreign Key (Admin_ID) REFERENCES admin_shop(Admin_ID)
);

-- maintains the relation between the delivery man and the order he is delivering
CREATE TABLE order_delivery_man(
    delivery_man_id INT NOT NULL, 
    Foreign Key (delivery_man_id) REFERENCES delivery_man(delivery_man_id);
    Order_ID INT NOT NULL,
    Foreign Key (Order_ID) REFERENCES orders(Order_ID);
    delivery_date DATETIME NOT NULL,
    PRIMARY KEY (delivery_man_id, Order_ID)
);

-- maintains all the orders in the order history of all customers
CREATE TABLE all_orders(
    Order_ID NOT NULL, 
    Foreign Key (Order_ID) REFERENCES orders(Order_ID),
    Product_ID INT NOT NULL,
    Foreign Key (Product_ID) REFERENCES product(Product_ID),
    product_quantity INT NOT NULL,
    product_price INT NOT NULL,
    Customer_ID INT NOT NULL,
    Foreign Key (Customer_ID) REFERENCES customer(Customer_ID),
    PRIMARY KEY (Order_ID, Product_ID, Customer_ID)
)


