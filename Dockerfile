# Use the Ubuntu 22.04 base image
FROM ubuntu:22.04

# Add Python 3.12 to the image
FROM python:3.12

# Update package lists for the Ubuntu system
RUN apt-get update

# Install the 'unzip' package
RUN apt install unzip

# Create and set working directory 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Get chrom using wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y

# Print the version of Google Chrome installed
RUN echo google-chrome --version

# Download chrome driver to match chrome version installed above 
RUN wget https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.42/linux64/chromedriver-linux64.zip

# Unzip chrome driver and move it to working directory
RUN unzip chromedriver-linux64.zip
RUN mv chromedriver-linux64 /usr/src/app/chromedriver

# Copy app requirements file and install using pip
COPY requirements.txt /usr/src/app
RUN pip install --requirement /usr/src/app/requirements.txt

# Copy python script to working directory of container 
COPY . /usr/src/app/

# Set default command to run when container starts
ENTRYPOINT ["python", "test_ryan_air_v2.py"]

# Optional entry point to keep container running for debug purposes
#ENTRYPOINT [ "tail", "-f", "/dev/null" ]
