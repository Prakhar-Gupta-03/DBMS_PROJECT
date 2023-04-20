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
        -- check if product quantity is valid
        if new.product_quantity <= 0 then
                signal sqlstate '45000' set message_text = 'Invalid product quantity';
        end if;
        -- check if product quantity is greater than available quantity
        if (select product_quantity from product where product_id = new.product_id) < new.product_quantity then
                signal sqlstate '45000' set message_text = 'Product quantity greater than available quantity';
        end if;
        -- check if product already exists in cart
        if (select count(*) from cart where product_id = new.product_id and customer_id = new.customer_id) > 0 then
                signal sqlstate '45000' set message_text = 'Product already exists in cart';
        end if;
end;

-- trigger to be executed before the product quantity is increased in the cart
create trigger increase_quantity before update on CART
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
        if (select product_quantity from product where product_id = new.product_id) < new.product_quantity + (select product_quantity from cart where product_id = new.product_id and customer_id = new.customer_id) then
                signal sqlstate '45000' set message_text = 'Product quantity greater than available quantity';
        end if;
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
        if (select customer_wallet from customer where customer_id =new.customer_id) < (select sum (product.product_price * cart.product_quantity) from product inner join cart on product.product_id = cart.product_id where cart.customer_id = new.customer_id) then
                signal sqlstate '45000' set message_text = 'Insufficient funds';
        end if;
        -- update customer wallet balance
        update customer set customer_wallet = customer_wallet - (select sum (product.product_price * cart.product_quantity) from product inner join cart on product.product_id = cart.product_id where cart.customer_id = new.customer_id) where customer_id = new.customer_id;
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

-- trigger to be executed before a category is added to the category table
create trigger add_category before insert on CATEGORY
for each row
begin
        -- check if the category already exists
        if (select count(*) from category where category_name = new.category_name) > 0 then
                signal sqlstate '45000' set message_text = 'Category already exists';
        end if;
end;