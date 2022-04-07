from .. import app
from pydantic import BaseModel, ValidationError

class City(BaseModel):
    #Queried city's name.
    name: str
    #Queried city's country code in the ISO 3166-1 alpha 3 format.
    country: str
    
class CityWeather(BaseModel):
    #Minimum temperature in degrees Celsius.
    min: float
    #Maximum temperature in degrees Celsius.
    max: float
    #Average temperature in degrees Celsius.
    avg: float
    #Feels like temperature in degrees Celsius.
    feels_like: float
    #city model
    city: City
    
def validate(original_result):
    city_weather = None
    try:
        city = City(
            name = original_result["name"],
            country = original_result["sys"]["country"]
        )
        city_weather = CityWeather(
            min = original_result["main"]["temp_min"],
            max = original_result["main"]["temp_max"],
            avg = original_result["main"]["temp"],
            feels_like = original_result["main"]["feels_like"],
            city = city
        )
    except ValidationError as e:
        app.logger.error(f"{e}")
    return city_weather