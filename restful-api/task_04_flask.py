#!/usr/bin/python3

"""
Simple Flask API
"""

from flask import Flask, request, jsonify

users = {}
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    """
    [GET] / route
    """
    return "Welcome to the Flask API!"


@app.route("/status", methods=['GET'])
def status():
    """
    [GET] /status route
    """
    return "OK"


@app.route("/data", methods=['GET'])
def get_users():
    """
    [GET] /data route
    """
    result = []
    for key in users.keys():
        result.append(key)

    return jsonify(result)


@app.route("/users/<username>", methods=['GET'])
def get_user(username: str):
    """
    [GET] /users/<username> route

    :param username: Username
    :type username: str
    """

    if username in users.keys():
        user = users[username]

        return jsonify({
            "username": username,
            "name": user['name'],
            "age": user['age'],
            "city": user['city']
        })

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    """
    [POST] /add_user route

    JSON: username, name, age, city
    """

    if request.get_json() is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = request.json.get('username', '')
    name = request.json.get('name', '')
    age = request.json.get('age', '')
    city = request.json.get('city', '')

    if username == "":
        return jsonify({"error": "Username is required"}), 400

    if username in users.keys():
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
    })


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
