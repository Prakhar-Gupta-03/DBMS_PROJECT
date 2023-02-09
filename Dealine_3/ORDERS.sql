USE test;
DROP TABLE ORDERS;
create table ORDERS (
	Delievery_Datetime DATE,
	Order_DateTime DATE,
	Order_id INT,
	-- Customer_iD INT AUTO_INCREMENT,
	Foreign Key (order_id) REFERENCES customer(Customer_id)
);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-05', '2023-01-18', 1);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-03', '2022-12-13', 2);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-02', '2023-01-20', 3);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-12', '2022-12-14', 4);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-22', '2022-12-26', 5);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-16', '2023-02-05', 6);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-27', '2022-12-31', 7);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-04', '2023-01-24', 8);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-26', '2022-12-10', 9);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-10', '2022-12-20', 10);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-14', '2023-01-08', 11);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-06', '2022-12-20', 12);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-16', '2023-02-04', 13);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-18', '2022-12-28', 14);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-19', '2023-01-25', 15);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-01', '2022-12-20', 16);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-24', '2022-12-20', 17);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-13', '2022-12-14', 18);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-04', '2022-12-25', 19);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-30', '2023-01-09', 20);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-14', '2023-01-12', 21);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-07', '2023-01-03', 22);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-26', '2023-01-30', 23);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-17', '2023-02-07', 24);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-11', '2023-01-22', 25);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-18', '2023-01-06', 26);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-18', '2023-02-04', 27);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-28', '2023-01-27', 28);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-22', '2022-12-24', 29);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-03', '2023-01-06', 30);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-02', '2022-12-20', 31);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-14', '2023-01-14', 32);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-02-22', '2023-01-01', 33);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-23', '2022-12-12', 34);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-18', '2022-12-12', 35);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-06', '2023-01-20', 36);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-04', '2023-01-19', 37);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-28', '2023-01-20', 38);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-17', '2023-01-21', 39);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-02-11', '2022-12-09', 40);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-22', '2023-01-25', 41);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-18', '2023-02-03', 42);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-27', '2023-01-22', 43);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-04', '2022-12-11', 44);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-20', '2023-02-06', 45);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-18', '2022-12-25', 46);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-01', '2022-12-23', 47);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-10', '2023-01-23', 48);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-06', '2023-01-15', 49);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-17', '2023-02-04', 50);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-04', '2023-02-04', 51);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-05', '2023-01-15', 52);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-13', '2022-12-13', 53);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-06', '2022-12-25', 54);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-22', '2023-01-24', 55);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-21', '2023-02-06', 56);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-17', '2023-02-04', 57);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-04', '2023-01-27', 58);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-02', '2022-12-15', 59);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-25', '2022-12-10', 60);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-02', '2022-12-09', 61);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-18', '2022-12-21', 62);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-07', '2022-12-12', 63);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-08', '2023-01-31', 64);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-01', '2023-01-02', 65);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-29', '2023-01-16', 66);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-01', '2023-02-07', 67);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-23', '2023-01-25', 68);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-22', '2023-01-30', 69);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-02', '2023-02-04', 70);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-20', '2023-01-27', 71);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-07', '2022-12-28', 72);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-19', '2023-02-02', 73);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-02-26', '2022-12-11', 74);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-07', '2022-12-26', 75);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-24', '2022-12-11', 76);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-02', '2023-01-31', 77);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-03', '2022-12-29', 78);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-05', '2023-01-28', 79);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-01', '2023-01-16', 80);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-23', '2022-12-19', 81);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-03', '2022-12-20', 82);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-26', '2022-12-20', 83);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-30', '2022-12-18', 84);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-02-23', '2022-12-12', 85);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-20', '2022-12-10', 86);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-18', '2022-12-30', 87);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-17', '2022-12-14', 88);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-08-19', '2022-12-19', 89);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-07-05', '2023-01-26', 90);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-09', '2023-02-08', 91);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-10-07', '2023-01-14', 92);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-03-10', '2023-01-17', 93);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-06-09', '2023-01-23', 94);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-27', '2023-01-05', 95);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-05-28', '2022-12-26', 96);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-02-26', '2022-12-28', 97);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-04-21', '2023-01-07', 98);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-11-22', '2023-01-01', 99);
insert into ORDERS (Delievery_Datetime, Order_DateTime, Order_id) values ('2022-09-11', '2023-01-04', 100);
