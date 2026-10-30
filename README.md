Incident Management System

Introduction

The Incident Management System is a web-based application used to create, track, assign, and resolve incidents related to infrastructure and applications.

Project Description

This project provides a simple web interface to manage incidents. Users can create incidents, view their details, set severity, assign incidents, and update their status.

Objective

The main objective of this project is to make incident tracking and management easier through a simple web-based application.

Technologies Used

Python

Flask

SQLite

HTML

Bootstrap

Docker

Docker Compose

Git and GitHub

Features

Create new incidents

View incident details

Set incident severity

Assign incidents to users

Resolve incidents

Store incident data using SQLite

Project Structure

app.py – Main Flask application

Dockerfile – Docker image configuration

docker-compose.yml – Runs the application using Docker Compose

requirements.txt – Python dependencies

templates/index.html – Web application interface

incidents.db – SQLite database

Steps Involved in Building the Project

Created a project directory.

Developed the application using Python and Flask.

Connected SQLite to store incident information.

Created the web interface using HTML and Bootstrap.

Added features to create, view, assign, and resolve incidents.

Created a Dockerfile to containerize the application.

Configured Docker Compose to run the application.

Built and started the Docker container.

Tested the application in the browser.

Uploaded the project source code to GitHub.

How to Run the Project

Clone the repository.

Open the project folder.

Run the following command:

docker compose up -d --build 

Open the browser and visit:

http://localhost:5000 

Conclusion

The Incident Management System project demonstrates how to build and run a web-based incident management application using Python, Flask, and SQLite. Docker and Docker Compose are used to containerize and run the application. This project helped in understanding web application development, database integration, containerization, and GitHub version control. 
