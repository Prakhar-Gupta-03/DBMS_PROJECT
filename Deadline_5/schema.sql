-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_shop`
--

DROP TABLE IF EXISTS `admin_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_shop` (
  `Admin_ID` int NOT NULL AUTO_INCREMENT,
  `ADMIN_NAME` varchar(50) NOT NULL,
  `Admin_Password` varchar(50) NOT NULL,
  PRIMARY KEY (`Admin_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `cart_ID` int NOT NULL AUTO_INCREMENT,
  `Customer_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  `product_quantity` int NOT NULL,
  `product_price` int NOT NULL,
  `order_ID` int DEFAULT NULL,
  `Admin_ID` int NOT NULL,
  PRIMARY KEY (`cart_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `Product_ID` (`Product_ID`),
  KEY `Admin_ID` (`Admin_ID`),
  KEY `order_ID` (`order_ID`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`Customer_ID`),
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`),
  CONSTRAINT `cart_ibfk_3` FOREIGN KEY (`Admin_ID`) REFERENCES `admin_shop` (`Admin_ID`),
  CONSTRAINT `cart_ibfk_4` FOREIGN KEY (`order_ID`) REFERENCES `orders` (`Order_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=248 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `Admin_ID` int NOT NULL,
  `Category_ID` int NOT NULL AUTO_INCREMENT,
  `Category_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Category_ID`),
  KEY `Admin_ID` (`Admin_ID`),
  CONSTRAINT `category_ibfk_1` FOREIGN KEY (`Admin_ID`) REFERENCES `admin_shop` (`Admin_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_fname` varchar(50) NOT NULL,
  `customer_lname` varchar(50) NOT NULL,
  `customer_email` varchar(50) NOT NULL,
  `customer_password` varchar(50) NOT NULL,
  `customer_wallet` int DEFAULT '0',
  `customer_contact_number` varchar(50) NOT NULL,
  `Customer_Address_BuildingNo` int NOT NULL,
  `Customer_Address_Street` varchar(50) NOT NULL,
  `Customer_Address_City` varchar(50) NOT NULL,
  `Customer_Address_State` varchar(50) NOT NULL,
  `Customer_Address_Pincode` varchar(10) NOT NULL DEFAULT '0',
  `Customer_ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Customer_ID`),
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `delivery_man`
--

DROP TABLE IF EXISTS `delivery_man`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_man` (
  `delivery_man_id` int NOT NULL AUTO_INCREMENT,
  `man_name` varchar(50) NOT NULL,
  `man_contact` varchar(15) NOT NULL,
  `man_email` varchar(50) NOT NULL,
  `man_pass` varchar(20) NOT NULL,
  `order_ID` int DEFAULT NULL,
  `Admin_ID` int NOT NULL,
  PRIMARY KEY (`delivery_man_id`),
  KEY `order_ID` (`order_ID`),
  KEY `Admin_ID` (`Admin_ID`),
  CONSTRAINT `delivery_man_ibfk_1` FOREIGN KEY (`order_ID`) REFERENCES `orders` (`Order_ID`),
  CONSTRAINT `delivery_man_ibfk_2` FOREIGN KEY (`Admin_ID`) REFERENCES `admin_shop` (`Admin_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `Order_ID` int NOT NULL AUTO_INCREMENT,
  `Customer_ID` int NOT NULL,
  `order_DateTime` datetime NOT NULL,
  `order_amount` int NOT NULL,
  `Admin_ID` int NOT NULL,
  PRIMARY KEY (`Order_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `Admin_ID` (`Admin_ID`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`Customer_ID`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`Admin_ID`) REFERENCES `admin_shop` (`Admin_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `Product_ID` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `product_price` int NOT NULL,
  `product_quantity` int NOT NULL,
  `Category_ID` int NOT NULL,
  `Admin_ID` int NOT NULL,
  PRIMARY KEY (`Product_ID`),
  KEY `Admin_ID` (`Admin_ID`),
  KEY `Category_ID` (`Category_ID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`Admin_ID`) REFERENCES `admin_shop` (`Admin_ID`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`Category_ID`) REFERENCES `category` (`Category_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-17 21:54:45
