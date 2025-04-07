# RyanAir Flight Booking Test App

## Python and Selenium based application to automate the search and booking of return flights with RyanAir airline.

_Developed and tested on Windows OS using Python 3.12.4. Tested using Chrome version 134 + related Chrome driver version_
_Chromedrive.exe in this repo is for Chrome version 134_

### Steps to run on Windows:
**_Pre-reqs_:** 
- _Python installed on local machine_
- _Chrome driver to match local Chrome version placed inside application directory_

1. Clone repo
   
   _git clone https://github.com/kmcc89/TestRyanAir.git_
  
3. Create virtual environment for application
   
   _python -m venv <virtual env name>_
   
5. Install dependencies using pip
   
   _pip install -r requirements.txt_

### Steps to run in Docker container:
**_Pre-req:_** 
- _Docker installed on local machine_
  
1. Clone repo
   
   _git clone https://github.com/kmcc89/TestRyanAir.git_
   
3. Build Docker image
   
   _docker build -t <image name> ._
   
5. Run Docker image
   
   _docker run <image name>_


### Python Program functionality:
1. Loads confguration details from json file (flight & passenger details + xpaths for webpage elements)
2. Sets up driver and loads webpage
3. Clears pop up windows (cookies and subscriber pop ups)
4. Enters departure, destination and dates for flights search
5. Enters number of passengers
6. Searches for available flights
7. Selects basic fare flight, skipds login step, enters passenger information
8. Current program stops at seat selection screen 

### Dockerfile functionality:
1. Sets up Ubuntu 22.04 and adds Python 3.12 runtime
2. Updates package lists for Ubuntu and installs unzip package
3. Creates directory for app to run in
4. Downloads and installs Chrome
5. Downloads, unzips and relocates chrome driver
6. Copies requirements file for application and uses pip to install dependencies
7. Copies remainder of application files
8. Executes Python program as Entrypoint for container when run 

