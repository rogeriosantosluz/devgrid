from crypt import methods
from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
from .. import app
from ..modules import weather
from ..modules.weather import cache

@app.route("/temperature/<city_name>", methods=["GET"])
def temperature_city_name(city_name):
    app.logger.info(f"city_name: {city_name}")
    ret = {
        "request": {
            "city_name": city_name
        }
    }
    city = weather.city_weather(city_name)
    ret["response"] = city
    return jsonify(ret)
    
@app.route("/temperature", methods=["GET"])
def temperature():
    app.logger.info("max: {}".format(request.args.get("max")))
    ret = {}
    try:
        if "max" not in request.args:
            ret["max"] = int(app.config['DEFAULT_MAX_NUMBER'])
        else:
            ret["max"] = int(request.args.get("max"))
    except Exception as e:
        ret["max"] = 5
    if ret["max"] > 0:
        counter = 0
        for k, v in cache.items():
            counter = counter + 1
            app.logger.info(f"{k[0]} => {v}")
            ret[k[0]] = v
            if ret["max"] == counter:
                break
    return jsonify(ret)
    
"""
@app.route("/not_covered", methods=["GET"])
def not_covered():
    return ""
"""