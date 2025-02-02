# BSE Stock Price Dashboard

## Introduction

This project is a **BSE Stock Price Dashboard** built using **Flask**. The dashboard allows users to view stock prices of a selected list of stocks. The project uses **Selenium**  or web scraping, and **Flask** to serve dashboard. This branch contains a variant that uses selenium with firefox browser with GeckoDriver and can be run locally using docker


#### 🌐 Deployment Variants

Currently two variants of this projects are live. more info of each variants can be found in their corresponding branches

| Variant | Branch              | Live Deployment |
|---------|---------------------|----------------|
| Splash  | `scrappy_deployment` | [BSE Dashboard](https://bse-dashboard-4xrp.onrender.com) |
| Vercel  | `vercel_branch`      | [BSE Dashboard](https://bse-dashboard.vercel.app/) |





## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.8.6-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-1.1.4-black?logo=flask)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-yellow?logo=selenium) 
![Firefox](https://img.shields.io/badge/Firefox-Browser-orange?logo=firefox) 
![GeckoDriver](https://img.shields.io/badge/GeckoDriver-Driver%20for%20Firefox-blue?logo=mozilla) 
![Requests](https://img.shields.io/badge/Requests-2.25.0-red?logo=python)
![Gunicorn](https://img.shields.io/badge/Gunicorn-20.0.4-green?logo=gunicorn)
![Jinja2](https://img.shields.io/badge/Jinja2-2.11.2-orange?logo=jinja)

## Setup and Installation

Follow these steps to set up and run the project locally
Clone the repo
   ```sh
    git clone https://github.com/paul-antony/bse_dashboard.git
   ```
build and run docker containers

```sh
docker-compose up --build
```

The Flask app will be accessible at
```
 http://localhost:5000
```
