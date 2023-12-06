# FitCal Pro
FitCal Pro is a versatile fitness tracker catering to diverse goals, from weight loss to professional sports. With an engaging user interface inspired by social media, it incorporates a dedicated progress tracker and a convenient 'new post' button for effortless logging of workouts and meals. The platform dynamically showcases personalized insights, including current goals, progress, and achievements based on user-logged data, enhancing the overall fitness journey.


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




