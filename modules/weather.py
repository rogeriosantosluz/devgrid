from .. import app
from flask import Blueprint
import click
import requests
import json
from ..models.weather import validate

bp = Blueprint("weather", __name__)

@bp.cli.command("cmd_city_weather")
@click.argument("city_name")
def cmd_city_weather(city_name):
    city_weather(city_name)

"""
Get the current temperature for the specified city_name, either from cache or from the Open Weather API, if not already cached (and still valid).
"""
def city_weather(city_name):
    result = {"status_code": -1, "response_text": "No response"}
    try:
        response = requests.get(f"{app.config['WEATHER_API']}?q={city_name}&appid={app.config['WEATHER_API_KEY']}")
        result["status_code"] = response.status_code
        app.logger.debug(f"response: {response}")
        app.logger.debug(f"response: {response.text}")
        original_result = json.loads(response.text)
        result["response_text"] = original_result
        #Validates and maps the original result to a pydantic model
        city_weather = validate(original_result)
        app.logger.debug(f"city_weather: {city_weather}")
        result["city_weather"] = city_weather.dict()
        del result["response_text"]
    except Exception as inst:
        error = str(type(inst).__name__) + "->" + str(inst)
        result["error"] = error
        app.logger.error(f"{error} - {result['status_code']} - {result['response_text']} ")
    return result
app.register_blueprint(bp)