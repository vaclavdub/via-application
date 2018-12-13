from flask import Flask
from flask import request
from flask_cors import CORS
import json
import time
import YelpSearch

flask = Flask(__name__)  # create flask
cors = CORS(flask)


@flask.route("/", methods=['GET'])  # define route
def get_hello_world():
    return "Hello world!"  # reply "Hello world" directly

@flask.route("/data", methods=['GET'])  # define route
def get_data():
    terms = "gluten-free"
    locations = "Klikatá 18, Praha"
    pole = YelpSearch.getRequest(terms, locations)
    return "".join(str(pole.pop().items()))

@flask.route("/date", methods=['GET'])
def get_date():
    date_var = time.strftime("%d/%m/%Y")
    return json.dumps({"date": date_var})  # create json and reply it


@flask.route("/time", methods=['GET'])
def get_time():
    time_var = time.strftime("%I:%M:%S")
    return json.dumps({"time": time_var})


@flask.route("/datetime", methods=['GET'])
def get_date_time():
    time_var = time.strftime("%I:%M:%S")
    date_var = time.strftime("%d/%m/%Y")
    return json.dumps({"time": time_var, "date": date_var})


@flask.route("/echo", methods=['POST'])  # returns back request content
def echo():
    request_json = request.json  # get json from request
    # here you can work with the data from json for example:
    author = request_json['author']
    message = request_json['message']
    return str(message) + " from " + str(author)
