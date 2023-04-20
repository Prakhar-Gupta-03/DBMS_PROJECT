USE test;

SELECT * from product;


-- -- query 1
-- -- What is the SQL query to retrieve the product details (ID and name) for products that belong to category 91 or 34?

-- SELECT category_ID,product_ID,product_name
--         FROM Product 
--         WHERE 
--         Category_ID = 91 or Category_ID=34;

-- -- query 2
-- -- Write a query to update the name of the admin to “Rahul” whose ID is 1

-- UPDATE ADMIN_SHOP 
--         SET ADMIN_NAME = 'Rahul' 
--         WHERE 
--         ADMIN_ID = 1;
-- SELECT ADMIN_NAME 
--         FROM ADMIN_SHOP 
--         WHERE 
--         ADMIN_ID = 1;

-- -- query 3
-- -- Write a query to update the name of the admin to “Anjali” whose ID is 1.

-- UPDATE ADMIN_SHOP 
--         SET ADMIN_NAME = 'Anjali' 
--         WHERE 
--         ADMIN_ID = 1;
-- SELECT ADMIN_NAME 
--         FROM ADMIN_SHOP 
--         WHERE 
--         ADMIN_ID = 1;


-- -- query 4
-- -- Write an SQL query to calculate the average order amount from the available data.

-- SELECT AVG(order_amount) FROM ORDERS;
-- SELECT * FROM DELIVERY_MAN;

-- -- query 5
-- --  What is an SQL query to count the number of orders whose order amount is more than 600?

-- SELECT ORDER_ID FROM ORDERS WHERE ORDER_AMOUNT > 600;

-- SELECT COUNT(ORDER_ID) FROM ORDERS WHERE ORDER_AMOUNT > 600;


-- -- query 6
-- -- Write a query to print all the products from the tables whose category is “Eggs” or “Milk”. 

-- SELECT * FROM PRODUCT WHERE CATEGORY_ID IN (SELECT CATEGORY_ID FROM CATEGORY WHERE CATEGORY_NAME = 'EGGS' OR CATEGORY_NAME = 'MILK');

-- -- query 7
-- -- Write a query to pick out all the cart details if the cart exists such that the prices of the product in the cart are greater than 1000
-- -- EXISTS query

-- SELECT CART_ID FROM CART WHERE EXISTS (SELECT CART_ID FROM CART WHERE PRODUCT_PRICE >1000 );

-- -- query 8
-- -- Write a query to change the customer table by adding a constraint that customer ID must always be unique.

-- ALTER TABLE CUSTOMER
-- ADD UNIQUE (CUSTOMER_ID);
-- SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = 1;

-- -- query 9 (i)
-- -- SINGLE INNER JOIN 
-- -- Write a query to show all the categories with their respective products sorted by the category ID. 

-- SELECT CATEGORY.CATEGORY_ID, CATEGORY.CATEGORY_NAME, PRODUCT.PRODUCT_ID, PRODUCT.PRODUCT_NAME 
-- FROM CATEGORY INNER JOIN PRODUCT 
-- ON CATEGORY.CATEGORY_ID = PRODUCT.CATEGORY_ID 
-- ORDER BY CATEGORY.CATEGORY_ID; 

-- -- query 9 (ii)
-- -- Write a query to display the categories with the amount of products for each category
-- -- GROUP BY Query

-- SELECT CATEGORY_ID, COUNT(PRODUCT_ID) FROM PRODUCT GROUP BY CATEGORY_ID;
-- d
-- -- query 10
-- -- DOUBLE INNER JOIN
-- -- What are the details of all the orders that have been delivered along with the delivery man and customer details?

-- SELECT DELIVERY_MAN.delivery_man_id, DELIVERY_MAN.man_name, 
-- ORDERS.ORDER_ID, ORDERS.order_amount, CUSTOMER.CUSTOMER_FNAME, 
-- CUSTOMER.Customer_Address_BuildingNo, CUSTOMER.Customer_Address_Street,
-- CUSTOMER.Customer_Address_City, CUSTOMER.Customer_Address_State, Customer_Address_Pincode 
-- FROM ORDERS INNER JOIN DELIVERY_MAN ON ORDERS.ORDER_ID = DELIVERY_MAN.ORDER_ID
-- INNER JOIN CUSTOMER ON ORDERS.CUSTOMER_ID = CUSTOMER.CUSTOMER_ID


