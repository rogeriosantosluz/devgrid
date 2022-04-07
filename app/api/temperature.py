from crypt import methods
from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
from .. import app
from ..modules import weather

@app.route("/temperature/<city_name>", methods=["GET"])
def temperature_city_name(city_name):
    app.logger.info(f"city_name: {city_name}")
    ret = {
        "request": {
            "city_name": city_name
        }
    }
    ret["response"] = weather.city_weather(city_name)
    return jsonify(ret)
    
@app.route("/temperature", methods=["GET"])
def temperature():
    app.logger.info("max: {}".format(request.args.get("max")))
    ret = {"status": "OK"}
    ret["max"] = request.args.get("max")
    return jsonify(ret)

"""
@app.route("/not_covered", methods=["GET"])
def not_covered():
    return ""
"""