-- aggregates sales by category and date, and calculates the total sales amount for each category and month
SELECT c.Category_Name, DATE_FORMAT(o.order_DateTime, '%Y-%m') AS Date,
       SUM(p.product_price * all_orders.product_quantity) AS Sales
FROM category c
JOIN product p ON c.Category_ID = p.Category_ID
JOIN all_orders ON p.Product_ID = all_orders.Product_ID
JOIN orders o ON all_orders.Order_ID = o.Order_ID
GROUP BY c.Category_Name, Date
ORDER BY Date, Sales DESC;




-- Top selling products by category
SELECT c.Category_Name, p.product_name,
       SUM(all_orders.product_quantity) AS Total_Quantity_Sold
FROM category c
JOIN product p ON c.Category_ID = p.Category_ID
JOIN all_orders ON p.Product_ID = all_orders.Product_ID
GROUP BY c.Category_Name, p.product_name
ORDER BY Total_Quantity_Sold DESC;


-- Revenue by customer location
SELECT Customer_Address_City, Customer_Address_State,
       SUM(p.product_price * all_orders.product_quantity) AS Revenue
FROM customer
JOIN all_orders ON customer.Customer_ID = all_orders.Customer_ID
JOIN product p ON all_orders.Product_ID = p.Product_ID
GROUP BY Customer_Address_City,



--  total revenue by month and category
SELECT DATE_FORMAT(order_DateTime, '%Y-%m') as Month, Category_Name, SUM(product_price * product_quantity) as Total_Sales
FROM product
JOIN category ON product.Category_ID = category.Category_ID
JOIN orders ON product.Admin_ID = orders.Admin_ID
GROUP BY Month, Category_Name;



