-- testing: write to here
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


DROP DATABASE IF EXISTS `fitcal` ;
CREATE DATABASE IF NOT EXISTS `fitcal` DEFAULT CHARACTER SET latin1 ;
USE `fitcal` ;


CREATE TABLE IF NOT EXISTS Store (
   storeID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(50),
   rating FLOAT,
   country VARCHAR(50),
   city VARCHAR(50),
   zip INT,
   street VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS Vegan_Alternatives (
   alternativeID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(50),
   price DECIMAL(10, 2), # supports up to $99,999,999.99
   calories INT,
   quantity INT
);


CREATE TABLE IF NOT EXISTS Nutrients (
   nutrientID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS Ingredients (
   ingredientID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(50),
   price DECIMAL(10, 2), # supports up to $99,999,999.99
   calories INT,
   quantity INT
);


CREATE TABLE IF NOT EXISTS Recipes (
   recipeID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(50),
   rating FLOAT,
   servingSize INT,
   allergens TEXT,
   calories INT,
   timeToMake TIME,
   steps TEXT
);

