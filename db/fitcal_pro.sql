-- testing: write to here
SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0;
SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'TRADITIONAL,ALLOW_INVALID_DATES';


DROP DATABASE IF EXISTS `fitcal`;
CREATE DATABASE IF NOT EXISTS `fitcal` DEFAULT CHARACTER SET latin1;
USE `fitcal`;


CREATE TABLE IF NOT EXISTS Store
(
    storeID INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(50),
    rating  FLOAT,
    country VARCHAR(50),
    city    VARCHAR(50),
    zip     INT,
    street  VARCHAR(50)
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
    price        DECIMAL(10, 2), # supports up to $99,999,999.99
    calories     INT,
    quantity     INT,
    isVegan      BOOLEAN
);

CREATE TABLE IF NOT EXISTS Store_Ingredients
(
    storeID      INT,
    ingredientID INT,
    PRIMARY KEY (storeID, ingredientID),
    FOREIGN KEY (storeID) REFERENCES Store (storeID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS VeganTips
(
    tipID INT AUTO_INCREMENT PRIMARY KEY,
    tip   TEXT
);

CREATE TABLE IF NOT EXISTS VeganTips_Store
(
    tipID   INT,
    storeID INT,
    PRIMARY KEY (tipID, storeID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (storeID) REFERENCES Store (storeID) ON UPDATE cascade ON DELETE cascade
);


CREATE TABLE IF NOT EXISTS Restaurant
(
    restaurantID    INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(50),
    cuisine         VARCHAR(50),
    rating          INT, # 1-10
    locationStreet  VARCHAR(50),
    locationCity    VARCHAR(50),
    locationCountry VARCHAR(50),
    locationZip     INT
);

CREATE TABLE IF NOT EXISTS VeganTips_Restaurant
(
    tipID   INT,
    restaurantID INT,
    PRIMARY KEY (tipID, restaurantID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (restaurantID) REFERENCES Restaurant (restaurantID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Meals
(
    mealID INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50),
    calories    INT,
    ingredients INT,
    isVegan BOOLEAN,
    FOREIGN KEY (ingredients) REFERENCES Ingredients (ingredientID) ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Meals_Restaurant
(
    mealID      INT,
    restaurantID INT,
    PRIMARY KEY (mealID, restaurantID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (restaurantID) REFERENCES Restaurant (restaurantID) ON UPDATE cascade ON DELETE cascade
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
    steps       TEXT
);

CREATE TABLE IF NOT EXISTS MealTracker
(
    mealTrackerID INT AUTO_INCREMENT PRIMARY KEY,
    mealDateTime  DATETIME
);

CREATE TABLE IF NOT EXISTS Exercise
(
    exerciseID INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50),
    weight     INT,
    reps       INT,
    difficulty INT, # 1-10
    equipment  VARCHAR(50),
    targetArea VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Routine
(
    routineID    INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    difficulty   INT, # 1-10
    timeDuration TIME
);

CREATE TABLE IF NOT EXISTS WorkoutTracker
(
    workoutID     INT AUTO_INCREMENT PRIMARY KEY,
    timeDuration  TIME,
    caloriesBurnt INT
);

CREATE TABLE IF NOT EXISTS Measurements
(
    measureID   INT AUTO_INCREMENT PRIMARY KEY,
    waterIntake INT,
    hoursSlept  INT,
    feetHeight  INT, # the 5 in 5'10
    inchHeight  INT, # the 10 in 5/10
    weight      INT  # lbs
);

CREATE TABLE IF NOT EXISTS DayTracker
(
    dayTrackerID INT AUTO_INCREMENT PRIMARY KEY,
    date         DATE
);

CREATE TABLE IF NOT EXISTS Profile
(
    username         VARCHAR(50) PRIMARY KEY,
    name             VARCHAR(50),
    bio              TEXT,
    registerDateTime DATETIME,
    birthDateTime    DATETIME
);
