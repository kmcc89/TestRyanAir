# RyanAir Flight Booking Test App

## Python and Selenium based application to automate the search and booking of return flights with RyanAir airline.

_Developed and tested on Windows OS using Python 3.12.4. Tested using Chrome version 135 + related Chrome driver version_

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

