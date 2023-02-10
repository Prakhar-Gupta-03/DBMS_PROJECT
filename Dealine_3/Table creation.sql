use test;
create table Admin(
    Admin_ID INT NOT NULL AUTO_INCREMENT,
    Admin_Password VARCHAR(20) NOT NULL,
    PRIMARY KEY (Admin_ID)
)
CREATE TABLE Product (
	Product_Name VARCHAR(50),
	Product_Quantity VARCHAR(50),
	Category_ID INT NOT NULL,
	Product_Price VARCHAR(50),
	Product_Offer VARCHAR(50),
	Product_ID INT NOT NULL,
    PRIMARY KEY (Category_ID)
    -- PRIMARY KEY (Category_ID)
);
CREATE TABLE category(
    Category_ID INT NOT NULL AUTO_INCREMENT,
    Sup_cat_ID INT,
    Category_Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Category_ID),
    FOREIGN KEY (Sup_cat_ID) REFERENCES Product(Category_ID)
);
create table cart(
    Cart_ID INT NOT NULL AUTO_INCREMENT,
    Cart_Total_Price INT NOT NULL, 
    Cart_Product_ID INT NOT NULL,
    Cart_Product_Quantity INT NOT NULL,
    PRIMARY KEY (Cart_ID),
    -- FOREIGN KEY (Cart_Product_ID) REFERENCES product(Product_ID)
);
create table customer(
    Customer_ID INT NOT NULL AUTO_INCREMENT, 
    Customer_First_Name VARCHAR(50) NOT NULL,
    Customer_Last_Name VARCHAR(50) NOT NULL,
    Customer_Address_BuildingNo VARCHAR(15) NOT NULL,
    Customer_Address_Street VARCHAR(50) NOT NULL,
    Customer_Address_City VARCHAR(50) NOT NULL,
    Customer_Address_State VARCHAR(50) NOT NULL,
    Customer_Address_Pincode VARCHAR(10) NOT NULL,
    Customer_Contact_Number VARCHAR(15) NOT NULL,
    Customer_Email VARCHAR(50) NOT NULL,
    Customer_Cart_ID INT NOT NULL,
    PRIMARY KEY (Customer_ID),
    FOREIGN KEY (Customer_Cart_ID) REFERENCES cart(Cart_ID)
);

create table order_details(
    Order_ID INT NOT NULL AUTO_INCREMENT, 
    Order_Date_Time DATETIME NOT NULL,
    Delivery_Date_Time DATETIME NOT NULL,
    Order_Customer_ID INT NOT NULL,
    PRIMARY KEY (Order_ID),
    FOREIGN KEY (Order_Customer_ID) REFERENCES customer(Customer_ID)
);
