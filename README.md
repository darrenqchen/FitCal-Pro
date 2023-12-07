# FitCal Pro
FitCal Pro is a versatile fitness tracker catering to diverse goals, from weight loss to professional sports. With an engaging user interface inspired by social media, it incorporates a dedicated progress tracker and a convenient 'new post' button for effortless logging of workouts and meals. The platform dynamically showcases personalized insights, including current goals, progress, and achievements based on user-logged data, enhancing the overall fitness journey.

## Overview

Video:

Appsmith repo: https://github.com/mdevine6427/FitCal-AppSmith

- Our application routes are split into 4 different blueprints:
    - Meals: Keeps track of all the food related tracking like meals, ingredients, recipes, nutrients, and vegantips
    - Fitness: Keeps track of all the fitness related tracking like routines and exercises
    - Tracking: Holds all the data for the trackers
    - Stores: Keeps track of all the external related data like stores and restaurants


## MySQL + Flask Project

This repo contains a setup for spinning up 3 Docker containers: 
1. A MySQL 8 container
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

- To connect to the database container use port 3200
- To connect to the web container use port 8001
- To connect to the appsmith container use port 8080
- To use the routes, you would use it like any other http request with GET, POST, PUT, and DELETE for the endpoints if they are there




