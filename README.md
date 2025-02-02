# BSE Stock Price Dashboard

## Introduction

This project is a **BSE Stock Price Dashboard** built using **Flask** and **Splash**. The dashboard allows users to view stock prices of a selected list of stocks. The project uses **Splash**, a headless browser service, for web scraping, and **Flask** to serve dashboard. Both the flask webserver and splash browser runs in seperate docker containers. the project is designed in such a way so it can be hosted in [Render](https://render.com/)

You can test the live version of the dashboard here: [BSE Dashboard](https://bse-dashboard-4xrp.onrender.com).

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-1.1.4-black?logo=flask)
![Requests](https://img.shields.io/badge/Requests-2.25.0-red?logo=python)
![Gunicorn](https://img.shields.io/badge/Gunicorn-20.0.4-green?logo=gunicorn)
![Jinja2](https://img.shields.io/badge/Jinja2-2.11.2-orange?logo=jinja)
![Splash](https://img.shields.io/badge/Splash-Headless%20Browser-orange?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Render](https://img.shields.io/badge/Render-Hosting-blue?logo=render)

## Setup and Installation

Follow these steps to set up and run the project locally or in a Dockerized environment.

```
docker-compose up --build
```

The Flask app will be accessible at
```
 http://localhost:5000
```

## Environment Variables

**SPLASH_URL**: The URL of the Splash service (default: http://splash-server:8050)

the url is used by flask to connct to splash to retrive the scrapped website contents
default value can be used when running locally using docker but the value needs to be updated in config if deployed to [Render](https://render.com/)

## Memory and Resource Limits

due to the free tier resource restrictions in [Render](https://render.com/), same restrictions are impossed in docker compose to run locally


