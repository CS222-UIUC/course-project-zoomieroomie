# How to run

## Prerequisites
* Python 3.6 or later installed
* pip package manager installed

## Steps
### 1. Open a terminal and navigate to the project directory.
### 2. Create a virtual environment by running the following command:

  `python -m venv env`

  This will create a new directory called venv which contains the Python virtual environment.

  Activate the virtual environment using the following command:
  `source venv/bin/activate`
  
  Or on Windows:
`env\Scripts\activate.bat`

### 3. Install Dependencies
Install the dependencies required for the project using the requirements.txt file using the following command:

`pip install -r requirements.txt`

### 4. Start the Backend Server
Navigate to the backend directory using the following command:

`cd main/backend`

Change the flask_app variable. This is a one time step:
`export FLASK_APP=run.py`

Run the backend server using the following command:

`flask run`

### 5. Start the Frontend Server
Open a new terminal window and navigate to the frontend/zoomie-roomie directory using the following command:

`cd frontend/zoomie-roomie`

Install the required packages using the following command (this is a one time step):
`npm install`

Run the frontend server using the following command:
`npm start`

