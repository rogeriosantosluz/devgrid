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

#Heroku Deploy
https://devgrid-weather-app.herokuapp.com/temperature/santos
https://devgrid-weather-app.herokuapp.com/temperature/taquara
https://devgrid-weather-app.herokuapp.com/temperature/ivoti
https://devgrid-weather-app.herokuapp.com/temperature/campinas
https://devgrid-weather-app.herokuapp.com/temperature/oxford
https://devgrid-weather-app.herokuapp.com/temperature/mongagua
https://devgrid-weather-app.herokuapp.com/temperature?max=3
https://devgrid-weather-app.herokuapp.com/temperature