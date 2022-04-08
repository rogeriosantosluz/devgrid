from flask import Flask
import json
import pytest
import requests
from pydantic import ValidationError
from ..api.temperature import *
from ..modules.weather import *
from ..models.weather import *

from .. import app

def test_temperature_many_cities():
    client = app.test_client()
    for city in ["santos", "campinas", "taquara", "parobe", "marilia", "ivoti"]:
        url = '/temperature/'+city
        response = client.get(url)
    response = client.get(url)    
    assert response.status_code == 200
    
def test_temperature_with_max():
    client = app.test_client()
    url = '/temperature?max=3'
    response = client.get(url)
    assert response.status_code == 200
    
def test_temperature_without_max():
    client = app.test_client()
    url = '/temperature'
    response = client.get(url)
    assert response.status_code == 200
    
def test_temperature_with_big_max():
    client = app.test_client()
    url = '/temperature?max=10000'
    response = client.get(url)
    assert response.status_code == 200
    
def test_temperature_max_as_str():
    client = app.test_client()
    url = '/temperature?max=ABC'
    response = client.get(url)
    assert response.status_code == 200
    
def test_original_result_key_error():
    with pytest.raises(KeyError):
        validate({"a":"b"})
        
def test_original_result_validation_error():
    with pytest.raises(ValidationError):
        validate({"name":1, "sys": {"country": "A"}, "main": {"temp_min":"A", "temp_max":2, "temp": 3, "feels_like":4}})
        
def test_city_weather_broken_url():
    app.config['WEATHER_API'] = "http://xxxx"
    assert "error" in city_weather("santos")
    
def test_city_weather_broken_api_key():
    app.config['WEATHER_API_KEY'] = "XXXX"
    assert "error" in city_weather("santos")
    
def test_city_weather_unknw_city():
    assert "error" in city_weather("xyz")