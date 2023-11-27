-- testing: write to here
SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0;
SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'TRADITIONAL,ALLOW_INVALID_DATES';


DROP DATABASE IF EXISTS `fitcal`;
CREATE DATABASE IF NOT EXISTS `fitcal` DEFAULT CHARACTER SET latin1;
USE `fitcal`;


CREATE TABLE IF NOT EXISTS Stores
(
    storeID INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(50),
    rating  FLOAT,
    street  VARCHAR(50),
    city    VARCHAR(50),
    zip     INT,
    country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Restaurants
(
    restaurantID INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    cuisine      VARCHAR(50),
    rating       FLOAT,
    street       VARCHAR(50),
    city         VARCHAR(50),
    country      VARCHAR(50),
    zip          INT
);

CREATE TABLE IF NOT EXISTS Nutrients
(
    nutrientID INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50),
    grams      INT
);

CREATE TABLE IF NOT EXISTS Ingredients
(
    ingredientID INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    price        DECIMAL(10, 2), -- supports up to $99,999,999.99
    calories     INT,
    quantity     INT,
    isVegan      BOOLEAN
);

CREATE TABLE IF NOT EXISTS VeganTips
(
    tipID INT AUTO_INCREMENT PRIMARY KEY,
    tip   TEXT
);

CREATE TABLE IF NOT EXISTS Recipes
(
    recipeID    INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50),
    rating      FLOAT,
    servingSize INT,
    allergens   TEXT,
    calories    INT,
    timeToMake  TIME,
    steps       TEXT,
    isVegan     BOOLEAN
);

CREATE TABLE IF NOT EXISTS Meals
(
    mealID      INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50),
    calories    INT,
    ingredients INT,
    isVegan     BOOLEAN,
    mealTrackerID INT,
    FOREIGN KEY (ingredients) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (mealTrackerID) REFERENCES MealTrackers (mealTrackerID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS MealTrackers
(
    mealTrackerID INT AUTO_INCREMENT PRIMARY KEY,
    dateTime      DATETIME,
    dayTrackerID  INT,
    FOREIGN KEY (dayTrackerID) REFERENCES DayTrackers (dayTrackerID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS DayTrackers
(
    dayTrackerID INT AUTO_INCREMENT PRIMARY KEY,
    date         DATE,
    username     VARCHAR(50),
    FOREIGN KEY (username) REFERENCES Profiles (username) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Profiles
(
    username         VARCHAR(50) PRIMARY KEY,
    firstName        VARCHAR(50),
    lastName         VARCHAR(50),
    bio              TEXT,
    registrationDate DATETIME,
    birthDate        DATETIME
);

CREATE TABLE IF NOT EXISTS Measurements
(
    measureID    INT AUTO_INCREMENT PRIMARY KEY,
    waterIntake  INT,
    hoursSlept   INT,
    heightFeet   INT, -- the 5 in 5'10''
    heightInches INT, -- the 10 in 5'10''
    weight       INT, -- lbs
    dayTrackerID INT,
    FOREIGN KEY (dayTrackerID) REFERENCES DayTrackers (dayTrackerID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS WorkoutTrackers
(
    workoutID     INT AUTO_INCREMENT PRIMARY KEY,
    timeDuration  TIME,
    caloriesBurnt INT,
    dayTrackerID  INT,
    FOREIGN KEY (dayTrackerID) REFERENCES DayTrackers (dayTrackerID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Routines
(
    routineID    INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    difficulty   INT, -- 1-10
    timeDuration TIME
);

CREATE TABLE IF NOT EXISTS Exercises
(
    exerciseID INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50),
    weight     INT,
    reps       INT,
    difficulty INT, -- 1-10
    equipment  VARCHAR(50),
    targetArea VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS VeganTips_Stores
(
    tipID   INT,
    storeID INT,
    PRIMARY KEY (tipID, storeID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (storeID) REFERENCES Stores (storeID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Stores_Ingredients
(
    storeID      INT,
    ingredientID INT,
    PRIMARY KEY (storeID, ingredientID),
    FOREIGN KEY (storeID) REFERENCES Stores (storeID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS VeganTips_Restaurants
(
    tipID        INT,
    restaurantID INT,
    PRIMARY KEY (tipID, restaurantID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (restaurantID) REFERENCES Restaurants (restaurantID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Meals_Restaurants
(
    mealID       INT,
    restaurantID INT,
    PRIMARY KEY (mealID, restaurantID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (restaurantID) REFERENCES Restaurants (restaurantID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Ingredients_Nutrients
(
    ingredientID INT,
    nutrientID   INT,
    PRIMARY KEY (ingredientID, nutrientID),
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (nutrientID) REFERENCES Nutrients (nutrientID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Recipes_Ingredients
(
    recipeID     INT,
    ingredientID INT,
    PRIMARY KEY (recipeID, ingredientID),
    FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS VeganTips_Recipes
(
    tipID    INT,
    recipeID INT,
    PRIMARY KEY (tipID, recipeID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Meals_Ingredients
(
    mealID       INT,
    ingredientID INT,
    PRIMARY KEY (mealID, ingredientID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Meals_Recipes
(
    mealID   INT,
    recipeID INT,
    PRIMARY KEY (mealID, recipeID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS WorkoutTrackers_Routines
(
    workoutID INT,
    routineID INT,
    PRIMARY KEY (workoutID, routineID),
    FOREIGN KEY (workoutID) REFERENCES WorkoutTrackers (workoutID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (routineID) REFERENCES Routines (routineID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Routines_Exercises
(
    routineID  INT,
    exerciseID INT,
    PRIMARY KEY (routineID, exerciseID),
    FOREIGN KEY (routineID) REFERENCES Routines (routineID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (exerciseID) REFERENCES Exercises (exerciseID) ON UPDATE cascade ON DELETE cascade
);