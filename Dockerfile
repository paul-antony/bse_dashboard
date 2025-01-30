# Use an official lightweight Python image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install GeckoDriver
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz" \
    -O /tmp/geckodriver.tar.gz && \
    tar -xvzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements file first (for better caching)
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port
EXPOSE 5000

# Set the command to start Flask (adjust if needed)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]