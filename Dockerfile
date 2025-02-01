FROM python:3.8-slim

# Install bash (it might already be included in some images, but we'll ensure it's there)
RUN apt-get update && apt-get install -y \
    bash \
    && apt-get clean

# Set the working directory inside the container (optional)
WORKDIR /opt/app

# Install Python dependencies if you have a requirements.txt (optional step)
# COPY requirements.txt /opt/app/
# RUN pip install --no-cache-dir -r requirements.txt

# Start a Bash shell when the container runs
CMD ["/bin/bash"]

# start comand : docker run -it -v C:/Users/paul/Desktop/bse_dashboard:/opt/app python-bash-container
