from flask import Flask
import json

from ..api.temperature import *
from .. import app

def test_temperature():
    client = app.test_client()
    url = '/temperature?max=100'
    response = client.get(url)
    assert response.status_code == 200
    
def test_temperature_city_name():
    client = app.test_client()
    url = '/temperature/santos'
    response = client.get(url)
    assert response.status_code == 200