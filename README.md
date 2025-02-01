# BSE Stock Price Dashboard

## Introduction

This project is a **BSE Stock Price Dashboard** built using **Flask** and **Splash**. The dashboard allows users to view stock prices of a selected list of stocks. The project uses **Splash**, a headless browser service, for web scraping, and **Flask** to serve dashboard. Both the flask webserver and splash browser runs in seperate docker containers. the project is designed in such a way so it can be hosted in [Render](https://render.com/)

you could test out the website hosted at https://bse-dashboard-4xrp.onrender.com



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


