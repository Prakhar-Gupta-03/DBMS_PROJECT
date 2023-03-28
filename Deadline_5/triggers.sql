USE TEST;
-- -- trigger to be executed before a product is added to the cart
create trigger add_to_cart before insert on CART
for each row
begin
        -- check if product exists
        if (select count(*) from product where product_id = new.product_id) = 0 then
                signal sqlstate '45000' set message_text = 'Product does not exist';
        end if;
        -- check if product is out of stock
        if (select product_quantity from product where product_id = new.product_id) <= 0 then
                signal sqlstate '45000' set message_text = 'Product out of stock';
        end if;
        -- check if product quantity is greater than available quantity
        if (select product_quantity from product where product_id = new.product_id) < new.product_quantity then
                signal sqlstate '45000' set message_text = 'Product quantity greater than available quantity';
        end if;
        -- check if product already exists in cart
        if (select count(*) from cart where product_id = new.product_id and customer_id = new.customer_id) > 0 then
                signal sqlstate '45000' set message_text = 'Product already exists in cart';
        end if;
        -- update product quantity in product table
        update product set product_quantity = product_quantity - new.product_quantity where product_id = new.product_id;
end;



-- trigger to be executed before a product is removed from a cart for a particular customer
create trigger remove_from_cart before delete on CART
for each row
begin
        -- trigger to be executed before a product is removed from a cart
        -- check if the product exists
        if (select count(*) from product where product_id = old.product_id) = 0 then
                signal sqlstate '45000' set message_text = 'Product does not exist';
        end if;
        -- check if the product exists in the cart
        if (select count(*) from cart where product_id = old.product_id and customer_id = old.customer_id) = 0 then
                signal sqlstate '45000' set message_text = 'Product does not exist in cart';
        end if;
        -- check if the customer exists
        if (select count(*) from customer where customer_id = old.customer_id) = 0 then
                signal sqlstate '45000' set message_text = 'Customer does not exist';
        end if;
        -- update product quantity in product table
        update product set product_quantity = product_quantity + old.product_quantity where product_id = old.product_id;
end;



-- trigger to be executed before an order is placed
create trigger place_order before insert on ORDERS
for each row
begin
        -- check if the customer exists
        if (select count(*) from customer where customer_id = new.customer_id) = 0 then
                signal sqlstate '45000' set message_text = 'Customer does not exist';
        end if;
        -- check if the customer has any products in the cart
        if (select count(*) from cart where customer_id = new.customer_id) = 0 then
                signal sqlstate '45000' set message_text = 'Cart is empty';
        end if;
        -- check if the customer has enough money to place the order
        if (select customer_wallet from customer where customer_id =new.customer_id) < (select sum(product_price * product_quantity) from product where product_id in (select product_id from cart where customer_id = new.customer_id)) then
                signal sqlstate '45000' set message_text = 'Insufficient funds';
        end if;
        -- update customer wallet balance
        update customer set customer_wallet = customer_wallet - (select sum(product_price * product_quantity) from product where product_id in (select product_id from cart where customer_id = new.customer_id)) where customer_id = new.customer_id;
end;

-- trigger to be executed after an order is placed
create trigger after_order after insert on ORDERS
for each row
begin 
        -- adding all the products from the cart to the all_orders table along with the order id
        insert into all_orders (order_id, product_id, product_quantity, product_price, customer_id) select new.order_id, (select product_id from cart where customer_id = new.customer_id), (select product_quantity from cart where customer_id = new.customer_id), (select product_price from product where product_id in (select product_id from cart where customer_id = new.customer_id)), new.customer_id from cart where customer_id = new.customer_id;
        -- assigning the delivery_man for the order which was just placed
        -- insert into order_delivery_man(delivery_man_id, new.order_id, order_date) select delivery_man_id, new.order_ID, now() from order_delivery_man group by delivery_man_id order by count(*) ASC LIMIT 1;
end;

-- trigger to be executed after deleting a product
create trigger delete_product_from_cart after delete on PRODUCT
for each row
begin 
        -- check if the product exists in the cart
        if (select count(*) from cart where product_id = old.product_id) > 0 then
                -- delete the product from the cart
                delete from cart where product_id = old.product_id;
        end if;

        -- check if the product exists in the orders
        if (select count(*) from all_orders where product_id = old.product_id) > 0 then
                -- delete the product from the orders
                delete from all_orders where product_id = old.product_id;
        end if;
end;

-- trigger to be executed after deleting a category
create trigger delete_category_from_cart after delete on CATEGORY
for each row
begin 
        -- check if the category exists in the product
        if (select count(*) from product where category_id = old.category_id) > 0 then
                -- delete all the products in that category
                delete from product where category_id = old.category_id;
                delete from cart where product_id in (select product_id from product where category_id = old.category_id);
        end if;
end;

-- trigger to be executed before a product is added to the product table
create trigger add_product before insert on PRODUCT
for each row
begin
        -- check if the category exists
        if (select count(*) from category where category_id = new.category_id) = 0 then
                signal sqlstate '45000' set message_text = 'Category does not exist';
        end if;
        -- check if the product already exists
        if (select count(*) from product where product_name = new.product_name) > 0 then
                signal sqlstate '45000' set message_text = 'Product already exists';
        end if;
        -- check if the product price is greater than 0
        if new.product_price <= 0 then
                signal sqlstate '45000' set message_text = 'Product price should be greater than 0';
        end if;
        -- check if the product quantity is greater than 0
        if new.product_quantity <= 0 then
                signal sqlstate '45000' set message_text = 'Product quantity should be greater than 0';
        end if;
end;

-- trigger to be executed before a product is deleted in the product table
create trigger delete_product before delete on PRODUCT
for each row
begin
        -- check if the product exists
        if (select count(*) from product where product_id = old.product_id) = 0 then
                signal sqlstate '45000' set message_text = 'Product does not exist';
        end if;
        -- check if the product exists in the cart
        if (select count(*) from cart where product_id = old.product_id) > 0 then
                -- delete the product from the cart
                delete from cart where product_id = old.product_id;
        end if;
end;

-- trigger to be executed before a category is deleted in the category table
create trigger delete_category before delete on CATEGORY
for each row
begin
        -- check if the category exists
        if (select count(*) from category where category_id = old.category_id) = 0 then
                signal sqlstate '45000' set message_text = 'Category does not exist';
        end if;
        -- for each product in the category delete the product from the cart
        if (select count(*) from product where category_id = old.category_id) > 0 then
                delete from cart where product_id in (select product_id from product where category_id = old.category_id);
        end if;
        -- delete all the products in that category
        delete from product where category_id = old.category_id;
end;

-- trigger to be executed before a product is updated in the product table
create trigger update_product before update on PRODUCT
for each row
begin
        -- check if the product exists
        if (select count(*) from product where product_id = new.product_id) = 0 then
                signal sqlstate '45000' set message_text = 'Product does not exist';
        end if;
end;