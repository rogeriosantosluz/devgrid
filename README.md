# devgrid
Flask Back-End Code Assessment Challenge


* python3 -m pip install --upgrade pip
* python3 -m venv env(PS> virtualenv env)
* source env/bin/activate (PS> .\env\Scripts\activate.bat)
* pip3 install -r requirements.txt
* export FLASK_ENV=development
* export set FLASK_APP=app.webapp (PS> $env:FLASK_APP="webapp")
* python3 -m flask run --host=0.0.0.0 (PS> flask run)

#Tests

* coverage run -m pytest
* coverage report -m