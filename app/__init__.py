import logging
import os
from flask import Flask
from .config import get_config

app = Flask(__name__)

app.config['SECRET_KEY'] = get_config("SECRET_KEY")
app.config['WEATHER_API'] = get_config("WEATHER_API")
app.config['WEATHER_API_KEY'] = get_config("WEATHER_API_KEY")
app.config['CACHE_TTL'] = get_config("CACHE_TTL")
app.config['DEFAULT_MAX_NUMBER'] = get_config("DEFAULT_MAX_NUMBER")

from .api import api

app.register_blueprint(api)

app.logger.info('App inicializada')