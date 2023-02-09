USE test;
DROP TABLE Product;
-- DESCRIBE Product;
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
-- -- INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Arizona - Plum Green Tea', '81881', 1, '100', '0', 1);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Tarragon - Primerba, Paste', '1841', 2, '100', '0', 2);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Appetizer - Mango Chevre', '65527', 3, '100', '0', 3);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Quail - Whole, Boneless', '03', 4, '100', '0', 4);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Beef Dry Aged Tenderloin Aaa', '6', 5, '100', '0', 5);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Rice - Aborio', '6', 6, '100', '0', 6);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Versatainer Nc - 8288', '8722', 7, '100', '0', 7);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Spoon - Soup, Plastic', '3', 8, '100', '0', 8);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Fish - Artic Char, Cold Smoked', '5', 9, '100', '0', 9);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Lettuce - Spring Mix', '38', 10, '100', '0', 10);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Chocolate - Dark Callets', '05', 11, '100', '0', 11);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cabbage - Nappa', '86572', 12, '100', '0', 12);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Ginsing - Fresh', '75', 13, '100', '0', 13);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Bread - Pita', '6385', 14, '100', '0', 14);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Octopus - Baby, Cleaned', '6', 15, '100', '0', 15);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Lemonade - Black Cherry, 591 Ml', '7', 16, '100', '0', 16);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Breadfruit', '0124', 17, '100', '0', 17);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Praline Paste', '2', 18, '100', '0', 18);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Paper Cocktail Umberlla 80 - 180', '418', 19, '100', '0', 19);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Lamb Shoulder Boneless Nz', '2675', 20, '100', '0', 20);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Milk Powder', '499', 21, '100', '0', 21);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Sour Puss - Tangerine', '3', 22, '100', '0', 22);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Tuna - Loin', '981', 23, '100', '0', 23);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cheese - Victor Et Berthold', '62276', 24, '100', '0', 24);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Onion Powder', '032', 25, '100', '0', 25);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Wine - Barolo Fontanafredda', '69716', 26, '100', '0', 26);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Table Cloth 62x120 White', '717', 27, '100', '0', 27);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cream - 35%', '635', 28, '100', '0', 28);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Munchies Honey Sweet Trail Mix', '875', 29, '100', '0', 29);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Pork - Backs - Boneless', '07', 30, '100', '0', 30);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Chip - Potato Dill Pickle', '07788', 31, '100', '0', 31);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Bacon Strip Precooked', '3664', 32, '100', '0', 32);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Bread Crumbs - Japanese Style', '061', 33, '100', '0', 33);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cheese - Comte', '010', 34, '100', '0', 34);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Container - Foam Dixie 12 Oz', '083', 35, '100', '0', 35);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Chinese Foods - Chicken Wing', '0020', 36, '100', '0', 36);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cake - Box Window 10x10x2.5', '4', 37, '100', '0', 37);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Napkin - Beverage 1 Ply', '401', 38, '100', '0', 38);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Plaintain', '96863', 39, '100', '0', 39);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Lobster - Base', '59', 40, '100', '0', 40);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Chinese Foods - Chicken Wing', '4471', 41, '100', '0', 41);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Quail - Jumbo', '3', 42, '100', '0', 42);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Beef - Tongue, Fresh', '3', 43, '100', '0', 43);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Passion Fruit', '6385', 44, '100', '0', 44);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cornflakes', '977', 45, '100', '0', 45);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Garlic - Primerba, Paste', '23536', 46, '100', '0', 46);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Tart - Raisin And Pecan', '95', 47, '100', '0', 47);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Oregano - Fresh', '33', 48, '100', '0', 48);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Sausage - Andouille', '53', 49, '100', '0', 49);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Calypso - Lemonade', '5', 50, '100', '0', 50);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Bread - Italian Sesame Poly', '730', 51, '100', '0', 51);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Pasta - Spaghetti, Dry', '86129', 52, '100', '0', 52);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Venison - Striploin', '530', 53, '100', '0', 53);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Sugar - Invert', '2', 54, '100', '0', 54);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Juice - Orange', '90780', 55, '100', '0', 55);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Corn Syrup', '58343', 56, '100', '0', 56);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Pastry - Mini French Pastries', '623', 57, '100', '0', 57);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Skirt - 29 Foot', '7257', 58, '100', '0', 58);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Wine - Balbach Riverside', '18513', 59, '100', '0', 59);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Chicken - Livers', '04', 60, '100', '0', 60);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Table Cloth 62x120 Colour', '4835', 61, '100', '0', 61);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cheese - Ricotta', '7175', 62, '100', '0', 62);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Beans - Butter Lrg Lima', '0', 63, '100', '0', 63);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Veal - Brisket, Provimi,bnls', '7', 64, '100', '0', 64);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Champagne - Brights, Dry', '27', 65, '100', '0', 65);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Taro Leaves', '6', 66, '100', '0', 66);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Gatorade - Orange', '1517', 67, '100', '0', 67);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Bandage - Fexible 1x3', '40520', 68, '100', '0', 68);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('External Supplier', '080', 69, '100', '0', 69);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Tomatoes - Cherry, Yellow', '9', 70, '100', '0', 70);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Schnappes Peppermint - Walker', '1', 71, '100', '0', 71);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Plate Pie Foil', '6', 72, '100', '0', 72);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Shrimp - Prawn', '24', 73, '100', '0', 73);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Bread - Sour Sticks With Onion', '53', 74, '100', '0', 74);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Compound - Rum', '03930', 75, '100', '0', 75);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Calypso - Pineapple Passion', '3658', 76, '100', '0', 76);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Dooleys Toffee', '4', 77, '100', '0', 77);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Appetizer - Spring Roll, Veg', '348', 78, '100', '0', 78);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Extract - Almond', '282', 79, '100', '0', 79);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Pepper - Green', '69018', 80, '100', '0', 80);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('The Pop Shoppe - Root Beer', '145', 81, '100', '0', 81);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Thyme - Lemon, Fresh', '9', 82, '100', '0', 82);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('French Pastry - Mini Chocolate', '36220', 83, '100', '0', 83);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Duck - Fat', '0', 84, '100', '0', 84);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Buttons', '05', 85, '100', '0', 85);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Pepper - Cayenne', '29083', 86, '100', '0', 86);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Vinegar - White', '11684', 87, '100', '0', 87);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Asparagus - Green, Fresh', '8', 88, '100', '0', 88);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Truffle Cups - Brown', '801', 89, '100', '0', 89);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Syrup - Golden, Lyles', '0516', 90, '100', '0', 90);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cotton Wet Mop 16 Oz', '2', 91, '100', '0', 91);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Red Cod Fillets - 225g', '95', 92, '100', '0', 92);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Butter - Salted, Micro', '65', 93, '100', '0', 93);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cake Circle, Foil, Scallop', '8334', 94, '100', '0', 94);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Island Oasis - Banana Daiquiri', '9769', 95, '100', '0', 95);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Sprouts - Alfalfa', '80', 96, '100', '0', 96);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Sauce - Cranberry', '49', 97, '100', '0', 97);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Lobster - Canned Premium', '3392', 98, '100', '0', 98);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Cabbage Roll', '31', 99, '100', '0', 99);
INSERT INTO Product (Product_Name, Product_Quantity, Category_ID, Product_Price, Product_Offer, Product_ID) VALUE ('Milk - 2% 250 Ml', '4955', 100, '100', '0', 100);

SELECT *FROM Product;
