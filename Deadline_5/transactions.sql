-- conflicting transaction 1
-- These two transactions conflict because the customer in transaction 1 is 
-- trying to buy the product for the original price, but the admin in transaction
--  2 has updated the price of the product

-- Transaction 1:
START TRANSACTION;
-- Adding a product to the cart
INSERT INTO cart (Customer_ID, Product_ID, product_quantity) 
VALUES (1, 1, 2);

-- Placing an order
INSERT INTO orders (Customer_ID, order_amount, order_DateTime, Admin_ID) 
VALUES (1, 100, NOW(), 1);

COMMIT;



-- Transaction 2:
START TRANSACTION;

-- Updating product price
UPDATE product 
SET product_price = 200 
WHERE Product_ID = 1;

COMMIT;

-- conflicting transaction 2
-- A customer adds a product to their cart and places an order,
--  but at the same time, the admin removes the product from the database.

-- Customer transaction
BEGIN;
INSERT INTO cart(Customer_ID, Product_ID, product_quantity) VALUES (1, 1, 1);
UPDATE product SET product_quantity = product_quantity - 1 WHERE Product_ID = 1;
COMMIT;

-- Admin transaction
BEGIN;
DELETE FROM product WHERE Product_ID = 1;
COMMIT;



-- Customer 1 transaction
BEGIN;
INSERT INTO cart(Customer_ID, Product_ID, product_quantity) VALUES (1, 1, 1);
COMMIT;

-- Customer 2 transaction
BEGIN;
INSERT INTO cart(Customer_ID, Product_ID, product_quantity) VALUES (2, 1, 1);
COMMIT;



-- conflicting transaction 3
-- Two customers try to buy the same product at the same time, but there is only one unit left


-- Customer 1 places order first
BEGIN;
UPDATE product SET product_quantity = product_quantity - 1 WHERE Product_ID = 1;
INSERT INTO orders(Customer_ID, order_amount, order_DateTime) VALUES (1, 100, NOW());
INSERT INTO all_orders(Order_ID, Product_ID, product_quantity, product_price, Customer_ID) 
SELECT Order_ID, Product_ID, product_quantity, product_price, Customer_ID 
FROM cart 
WHERE Customer_ID = 1;
DELETE FROM cart WHERE Customer_ID = 1;
COMMIT;

-- Customer 2 places order after Customer 1
BEGIN;
UPDATE product SET product_quantity = product_quantity - 1 WHERE Product_ID = 1;
INSERT INTO orders(Customer_ID, order_amount, order_DateTime) VALUES (2, 100, NOW());
INSERT INTO all_orders(Order_ID, Product_ID, product_quantity, product_price, Customer_ID) 
SELECT Order_ID, Product_ID, product_quantity, product_price, Customer_ID 
FROM cart 
WHERE Customer_ID = 2;
DELETE FROM cart WHERE Customer_ID = 2;
COMMIT;


-- conflicting transaction 4
-- A delivery man accepts an order, but at the same time, the admin deletes the product from the database.

-- Delivery man transaction
BEGIN;
INSERT INTO order_delivery_man(Delivery_Man_ID, Order_ID, delivery_date) VALUES (1, 1, NOW());
COMMIT;

-- Admin transaction
BEGIN;
DELETE FROM product WHERE Product_ID = 1;
COMMIT;









-- Non-conflicting transaction 1

-- adds a new product to the customer's cart and updates the product quantity in the inventory
BEGIN TRANSACTION;

-- Add a new product to the cart
INSERT INTO cart(Customer_ID, Product_ID, product_quantity)
VALUES(1, 5, 2);

-- Update the product quantity in the inventory
UPDATE product SET product_quantity = product_quantity - 2 WHERE Product_ID = 5;

COMMIT;

-- Non-conflicting transaction 2

-- places a new order and adds the products from the customer's cart to the order history


BEGIN TRANSACTION;

-- Place a new order
INSERT INTO orders(Customer_ID, order_amount, order_DateTime, Admin_ID)
VALUES(1, 2000, NOW(), 1);

-- Insert the products in the order history
INSERT INTO all_orders(Order_ID, Product_ID, product_quantity, product_price, Customer_ID)
SELECT orders.Order_ID, cart.Product_ID, cart.product_quantity, product.product_price, cart.Customer_ID
FROM orders
JOIN cart ON orders.Customer_ID = cart.Customer_ID
JOIN product ON cart.Product_ID = product.Product_ID
WHERE orders.Customer_ID = 1;

COMMIT;







