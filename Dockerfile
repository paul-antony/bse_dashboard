# Copy only requirements file first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Google Chrome (for headless browsing or automation)
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Now copy the rest of the application files
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Set the command to start Flask (adjust if needed)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]