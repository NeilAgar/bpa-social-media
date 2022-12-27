### How to Run -

    Pre-requirements:
     - Python3 (3.8+) and pip must be installed
     - No other service must be running on port 5000 while the app is running
     - A MongoDB Server owned or able to be used by you (must have access to the server URI) 

1. Create the virtual environment
   - Change directory to the project
   - Create a python virtual environment named "venv" by entering `python3 -m venv venv` into the command prompt or terminal
   - Once it is created, type the following into the terminal depending on your OS
     - MacOS / Linux:
       - `source venv/bin/activate`
     - Windows - Using cmd.exe:
       - `venv\Scripts\activate.bat`
     - Windows - Using Powershell:
       - `venv\Scripts\Activate.ps1`


2. Install pip requirements
   - Inside of the venv, type the following depending on the os
     - MacOS:
       - `python -m pip install -r requirements.txt`
     - Windows:
       - `py -m pip install -r requirements.txt` or `python -m pip install -r requirements.txt`


3. Edit configurations / settings
   - Inside of the project is a .env file
     - Your file viewer may hide files that start with a .
     - On Windows, go to the view window at the top and make sure Hidden items and File name extensions are both checked
     - On Mac, press cmd + shift + .
     - On Linux, press ctrl + h
   - Open the .env file
     - Replace the `MONGODB_URL` field with the URI to your mongodb server
     - Ex: `MONGODB_URL="mongodb://127.0.0.1:27017/"`
     - Next, find the `DATABASE_NAME` field which will be the name of the database used by the app
     - Ex: `DATABASE_NAME="BPAV04"`


4. Run App
   - Once in the venv with all configurations and requirements met, run the main file
     - MacOS / Linux:
       - `python3 app.py`
     - Windows:
       - `py app.py` or `python app.py`
   - The app should be running, and a URL should be presented in the console
     - It is likely `127.0.0.1:5000` or `localhost:5000`