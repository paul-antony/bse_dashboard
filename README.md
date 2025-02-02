# BSE Stock Price Dashboard

## Introduction

This project is a **BSE Stock Price Dashboard** built using **Flask**. The dashboard allows users to view stock prices of a selected list of stocks. The project uses python module [**bsedata**](https://github.com/sdabhi23/bsedata) for web scraping, and **Flask** to serve dashboard. the project is designed in such a way so it can be hosted in [Vercel](https://vercel.com/)

You can test the live version of the dashboard here: [BSE Dashboard](https://bse-dashboard.vercel.app/).

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.8.6-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-1.1.4-black?logo=flask)
![BSEData](https://img.shields.io/badge/BSEData-Stock%20Market%20API-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-2.25.0-red?logo=python)
![Gunicorn](https://img.shields.io/badge/Gunicorn-20.0.4-green?logo=gunicorn)
![Jinja2](https://img.shields.io/badge/Jinja2-2.11.2-orange?logo=jinja)
![Vercel](https://img.shields.io/badge/Vercel-Hosting-black?logo=vercel)
## Setup and Installation

Follow these steps to set up and run the project locally
Clone the repo
   ```sh
    git clone -b vercel_branch https://github.com/paul-antony/bse_dashboard.git
   ```
 
**Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate
```

Install requirments
   ```sh
    pip install -r requirements.txt
   ```

Start the flask server
   ```sh
    python main.py runserver
   ```

The Flask app will be accessible at
```
 http://localhost:5000
```


