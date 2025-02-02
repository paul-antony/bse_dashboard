#Use an official lightweight Python image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    unzip \
    xvfb \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    libxrender1 \
    libasound2 \
    libnss3 \
    libx11-xcb1

# Install a stable version of GeckoDriver (specify a known good version)
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz" \
    -O /tmp/geckodriver.tar.gz && \
    tar -xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz


# Set the Firefox binary location explicitly
ENV FIREFOX_BIN=/usr/bin/firefox


# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port
EXPOSE 5000

# Command to run Flask app with Gunicorn (or just flask for development)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]