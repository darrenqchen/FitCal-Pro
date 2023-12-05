SET
    @OLD_UNIQUE_CHECKS = @UNIQUE_CHECKS,
    UNIQUE_CHECKS = 0;

SET
    @OLD_FOREIGN_KEY_CHECKS = @FOREIGN_KEY_CHECKS,
    FOREIGN_KEY_CHECKS = 0;

SET
    @OLD_SQL_MODE = @SQL_MODE,
    SQL_MODE = 'TRADITIONAL,ALLOW_INVALID_DATES';

DROP DATABASE IF EXISTS `fitcal`;

CREATE DATABASE IF NOT EXISTS `fitcal` DEFAULT CHARACTER SET latin1;

USE `fitcal`;

-- ======================== Main Table Creation ========================
CREATE TABLE IF NOT EXISTS Stores (
    storeID INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(50),
    rating  FLOAT,
    street  VARCHAR(50),
    city    VARCHAR(50),
    zip     VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Restaurants (
    restaurantID INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    cuisine      VARCHAR(50),
    rating       FLOAT,
    street       VARCHAR(50),
    city         VARCHAR(50),
    country      VARCHAR(50),
    zip          VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Nutrients (
    nutrientID INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50),
    grams      INT
);

CREATE TABLE IF NOT EXISTS Ingredients (
    ingredientID INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    price        DECIMAL(10, 2),
    -- supports up to $99,999,999.99
    calories     INT,
    quantity     INT,
    isVegan      BOOLEAN
);

CREATE TABLE IF NOT EXISTS VeganTips (
    tipID INT AUTO_INCREMENT PRIMARY KEY,
    tip   TEXT
);

CREATE TABLE IF NOT EXISTS Recipes (
    recipeID    INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50),
    rating      FLOAT,
    servingSize INT,
    allergens   TEXT,
    calories    INT,
    timeToMake  INT, -- in minutes
    steps       TEXT,
    isVegan     BOOLEAN
);

CREATE TABLE IF NOT EXISTS Meals (
    mealID        INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(50),
    calories      INT,
    isVegan       BOOLEAN,
    mealTrackerID INT,
    FOREIGN KEY (mealTrackerID) REFERENCES MealTrackers (mealTrackerID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS MealTrackers (
    mealTrackerID INT AUTO_INCREMENT PRIMARY KEY,
    mealDateTime  DATETIME,
    dayTrackerID  INT,
    FOREIGN KEY (dayTrackerID) REFERENCES DayTrackers (dayTrackerID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS DayTrackers (
    dayTrackerID INT AUTO_INCREMENT PRIMARY KEY,
    date         DATE,
    username     VARCHAR(50),
    FOREIGN KEY (username) REFERENCES Profiles (username) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Profiles (
    username         VARCHAR(50) PRIMARY KEY,
    firstName        VARCHAR(50),
    lastName         VARCHAR(50),
    bio              TEXT,
    registrationDate DATETIME,
    birthDate        DATETIME
);

CREATE TABLE IF NOT EXISTS Measurements (
    measureID    INT AUTO_INCREMENT PRIMARY KEY,
    waterIntake  FLOAT,
    hoursSlept   FLOAT,
    heightFeet   INT, -- the 5 in 5'10''
    heightInches INT, -- the 10 in 5'10''
    weight       FLOAT, -- lbs
    dayTrackerID INT,
    FOREIGN KEY (dayTrackerID) REFERENCES DayTrackers (dayTrackerID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS WorkoutTrackers (
    workoutID     INT AUTO_INCREMENT PRIMARY KEY,
    timeDuration  TIME,
    caloriesBurnt INT,
    dayTrackerID  INT,
    FOREIGN KEY (dayTrackerID) REFERENCES DayTrackers (dayTrackerID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Routines (
    routineID    INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(50),
    difficulty   FLOAT,
    timeDuration INT -- minutes
);

CREATE TABLE IF NOT EXISTS Exercises (
    exerciseID INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50),
    weight     INT,
    reps       INT,
    difficulty FLOAT,
    equipment  VARCHAR(50),
    targetArea VARCHAR(50)
);

-- ======================== M:N Relationship Tables ===============================
CREATE TABLE IF NOT EXISTS VeganTips_Stores (
    tipID   INT,
    storeID INT,
    PRIMARY KEY (tipID, storeID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (storeID) REFERENCES Stores (storeID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Stores_Ingredients (
    storeID      INT,
    ingredientID INT,
    PRIMARY KEY (storeID, ingredientID),
    FOREIGN KEY (storeID) REFERENCES Stores (storeID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS VeganTips_Restaurants (
    tipID        INT,
    restaurantID INT,
    PRIMARY KEY (tipID, restaurantID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (restaurantID) REFERENCES Restaurants (restaurantID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Meals_Restaurants (
    mealID       INT,
    restaurantID INT,
    PRIMARY KEY (mealID, restaurantID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (restaurantID) REFERENCES Restaurants (restaurantID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Ingredients_Nutrients (
    ingredientID INT,
    nutrientID   INT,
    PRIMARY KEY (ingredientID, nutrientID),
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (nutrientID) REFERENCES Nutrients (nutrientID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Recipes_Ingredients (
    recipeID     INT,
    ingredientID INT,
    PRIMARY KEY (recipeID, ingredientID),
    FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS VeganTips_Recipes (
    tipID    INT,
    recipeID INT,
    PRIMARY KEY (tipID, recipeID),
    FOREIGN KEY (tipID) REFERENCES VeganTips (tipID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Meals_Ingredients (
    mealID       INT,
    ingredientID INT,
    PRIMARY KEY (mealID, ingredientID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Meals_Recipes (
    mealID   INT,
    recipeID INT,
    PRIMARY KEY (mealID, recipeID),
    FOREIGN KEY (mealID) REFERENCES Meals (mealID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS WorkoutTrackers_Routines (
    workoutID INT,
    routineID INT,
    PRIMARY KEY (workoutID, routineID),
    FOREIGN KEY (workoutID) REFERENCES WorkoutTrackers (workoutID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (routineID) REFERENCES Routines (routineID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Routines_Exercises (
    routineID  INT,
    exerciseID INT,
    PRIMARY KEY (routineID, exerciseID),
    FOREIGN KEY (routineID) REFERENCES Routines (routineID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (exerciseID) REFERENCES Exercises (exerciseID) ON UPDATE CASCADE ON DELETE CASCADE
);

# -- ========================= Data Entries =====================
# -- Stores
# INSERT INTO Stores (name, rating, country, city, zip, street)
# VALUES ('Stop & Shop',
#         8.3,
#         'US',
#         'Boston',
#         02120,
#         'Tremont St');
#
# INSERT INTO Stores (name, rating, country, city, zip, street)
# VALUES ('Star Market',
#         8,
#         'US',
#         'Boston',
#         02115,
#         'Huntington Ave');
#
# -- Restaurants
# INSERT INTO Restaurants (name,
#                          cuisine,
#                          rating,
#                          country,
#                          city,
#                          zip,
#                          street)
# VALUES ('El Jefes',
#         'Mexican',
#         9,
#         'US',
#         'Boston',
#         02115,
#         'Huntington Ave');
#
# INSERT INTO Restaurants (name,
#                          cuisine,
#                          rating,
#                          country,
#                          city,
#                          zip,
#                          street)
# VALUES ('Milkweed',
#         'American',
#         9.2,
#         'US',
#         'Boston',
#         02120,
#         'Tremont St');
#
# -- Nutrients
# INSERT INTO Nutrients (name, grams)
# VALUES ('protein', 10);
#
# INSERT INTO Nutrients (name, grams)
# VALUES ('carbs', 5);
#
# -- Ingredients
# INSERT INTO Ingredients (price, quantity, calories, name, isVegan)
# VALUES (6.45, 10, 100, 'sugar', 1);
#
# INSERT INTO Ingredients (price, quantity, calories, name, isVegan)
# VALUES (15.67, 10, 80, 'chicken breast', 0);
#
# -- VeganTips
# INSERT INTO VeganTips (tip)
# VALUES ('Do not eat meat');
#
# INSERT INTO VeganTips (tip)
# VALUES ('Do eat veggie');
#
# -- Recipes
# INSERT INTO Recipes (steps,
#                      timeToMake,
#                      calories,
#                      allergens,
#                      name,
#                      rating,
#                      servingSize,
#                      isVegan)
# VALUES ('1. crack eggs  2. scramble them',
#         5,
#         20,
#         'egg',
#         'scrambled egg',
#         6,
#         1,
#         0);
#
# INSERT INTO Recipes (steps,
#                      timeToMake,
#                      calories,
#                      allergens,
#                      name,
#                      rating,
#                      servingSize,
#                      isVegan)
# VALUES ('1. wash vegetable  2. chop them  3. mix them with dressing',
#         10,
#         20,
#         'none',
#         'salad',
#         5,
#         2,
#         1);
#
# -- Meals
# INSERT INTO Meals (name,
#                    calories,
#                    isVegan,
#                    mealTrackerID)
# VALUES ('Chicken Parm', 90, 0, 1);
#
# INSERT INTO Meals (name,
#                    calories,
#                    isVegan,
#                    mealTrackerID)
# VALUES ('Salad', 20, 1, 2);
#
# -- MealTrackers
# INSERT INTO MealTrackers (mealDateTime, dayTrackerID)
# VALUES (NOW(), 1);
#
# INSERT INTO MealTrackers (mealDateTime, dayTrackerID)
# VALUES (NOW(), 2);
#
# -- DayTrackers
# INSERT INTO DayTrackers (date, username)
# VALUES ('2023-11-26', 'darrenchen');
#
# INSERT INTO DayTrackers (date, username)
# VALUES ('2023-11-25', 'billxu');
#
# -- Profiles
# INSERT INTO Profiles (username,
#                       firstName,
#                       lastName,
#                       bio,
#                       registrationDate,
#                       birthDate)
# VALUES ('darrenchen',
#         'Darren',
#         'Chen',
#         'senior CS student at Northeastern',
#         '2020-09-08 15:10:10',
#         '1970-01-01 00:00:01');
#
# INSERT INTO Profiles (username,
#                       firstName,
#                       lastName,
#                       bio,
#                       registrationDate,
#                       birthDate)
# VALUES ('billxu',
#         'Bill',
#         'Xu',
#         'amazon dude',
#         '2021-01-19 03:14:07',
#         '1981-08-03 03:10:12');
#
# -- Measurements
# INSERT INTO Measurements (waterIntake,
#                           hoursSlept,
#                           heightFeet,
#                           heightInches,
#                           weight,
#                           dayTrackerID)
# VALUES (10.2, 8, 6, 0, 150, 1);
#
# INSERT INTO Measurements (waterIntake,
#                           hoursSlept,
#                           heightFeet,
#                           heightInches,
#                           weight,
#                           dayTrackerID)
# VALUES (8, 6.5, 5, 10, 131.3, 2);
#
# -- WorkoutTrackers
# INSERT INTO WorkoutTrackers (timeDuration, caloriesBurnt, dayTrackerID)
# VALUES ('2:12:01', 100, 1);
#
# INSERT INTO WorkoutTrackers (timeDuration, caloriesBurnt, dayTrackerID)
# VALUES ('6:13:02', 321, 2);
#
# -- Routines
# INSERT INTO Routines (name, difficulty, timeDuration)
# VALUES ('Push Pull Legs', 7, '2:12:01');
#
# INSERT INTO Routines (name, difficulty, timeDuration)
# VALUES ('Ab Circuit', 5, '6:13:02');
#
# -- Exercises
# INSERT INTO Exercises (name,
#                        weight,
#                        reps,
#                        difficulty,
#                        equipment,
#                        targetArea)
# VALUES ('chest press', 50, 5, 7, 'dumbbell', 'chest');
#
# INSERT INTO Exercises (name,
#                        weight,
#                        reps,
#                        difficulty,
#                        equipment,
#                        targetArea)
# VALUES ('deadlift', 315, 2, 9, 'barbell', 'chest');
#
# -- VeganTips_Stores
# INSERT INTO VeganTips_Stores
# VALUES (1, 1);
#
# INSERT INTO VeganTips_Stores
# VALUES (2, 2);
#
# -- Stores_Ingredients
# INSERT INTO Stores_Ingredients
# VALUES (1, 1);
#
# INSERT INTO Stores_Ingredients
# VALUES (2, 2);
#
# -- VeganTips_Restaurants
# INSERT INTO VeganTips_Restaurants
# VALUES (1, 1);
#
# INSERT INTO VeganTips_Restaurants
# VALUES (2, 2);
#
# -- Meals_Restaurants
# INSERT INTO Meals_Restaurants
# VALUES (1, 1);
#
# INSERT INTO Meals_Restaurants
# VALUES (2, 2);
#
# -- Ingredients_Nutrients
# INSERT INTO Ingredients_Nutrients
# VALUES (1, 1);
#
# INSERT INTO Ingredients_Nutrients
# VALUES (2, 2);
#
# -- Recipes_Ingredients
# INSERT INTO Recipes_Ingredients
# VALUES (1, 1);
#
# INSERT INTO Recipes_Ingredients
# VALUES (2, 2);
#
# -- VeganTips_Recipes
# INSERT INTO VeganTips_Recipes
# VALUES (1, 1);
#
# INSERT INTO VeganTips_Recipes
# VALUES (2, 2);
#
# -- Meals_Ingredients
# INSERT INTO Meals_Ingredients
# VALUES (1, 1);
#
# INSERT INTO Meals_Ingredients
# VALUES (2, 2);
#
# -- Meals_Recipes
# INSERT INTO Meals_Recipes
# VALUES (1, 1);
#
# INSERT INTO Meals_Recipes
# VALUES (2, 2);
#
# -- WorkoutTrackers_Routines
# INSERT INTO WorkoutTrackers_Routines
# VALUES (1, 1);
#
# INSERT INTO WorkoutTrackers_Routines
# VALUES (2, 2);
#
# -- Routines_Exercises
# INSERT INTO Routines_Exercises
# VALUES (1, 1);
#
# INSERT INTO Routines_Exercises
# VALUES (2, 2);