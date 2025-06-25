from flask import Flask
import json


app = Flask(__name__)
current_version: str = "1.0.0"


# videos api, models api
# store statistics in json files, load them first
# videos api -> number of views
# models api -> number of model views

@app.route("/api/dashboard/v1/version", methods=['GET'])
def get_version():
    response = {}
    data = {}

    data["version"] = current_version
    response["status_code"] = "200"
    response["data"] = data

    string_response: str = json.dumps(response)
    return string_response

@app.route("/api/dashboard/v1/version/<user>", methods=['GET'])
def get_user_version(user: str):
    response = {}
    data = {}

    data["version"] = current_version
    data["user"] = user
    response["status_code"] = "200"
    response["data"] = data

    string_response: str = json.dumps(response)
    return string_response