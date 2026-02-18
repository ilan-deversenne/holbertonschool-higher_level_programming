#!/usr/bin/python3

"""
Simple Flask API
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


class User:
    """
    User class
    """
    users = []

    def __init__(self, username: str, name: str, age: int, city: str) -> None:
        """
        Create a user (without store)

        :param self: Self object
        :param username: Username
        :type username: str
        :param name: Name
        :type name: str
        :param age: Age
        :type age: int
        :param city: City
        :type city: str
        """
        self.username = username
        self.name = name
        self.age = age
        self.city = city

    def store(self):
        """
        Store the user into the users list

        :param self: Self object
        """
        User.users.append(self)

    def json(self) -> dict:
        """
        Dict for searilize object

        :param self: Self object
        :return: List of attributs
        :rtype: dict
        """

        return self.__dict__

    @staticmethod
    def username_taken(username: str) -> bool:
        """
        Check if a username is arealy used

        :param username: Description
        :type username: str
        :return: True if the username is arealy taken else False
        :rtype: bool
        """
        for user in User.users:
            if user.username == username:
                return True

        return False

    @staticmethod
    def by_username(username: str):
        """
        Get a stored user by his username

        :param username: Username
        :type username: str
        """
        for user in User.users:
            if user.username == username:
                return user


@app.route("/", methods=['GET'])
def index():
    return "Welcome to the Flask API!"


@app.route("/status", methods=['GET'])
def status():
    return "OK"


@app.route("/users", methods=['GET'])
def get_users():
    result = []
    for user in User.users:
        result.append(user.username)

    return jsonify(result)


@app.route("/users/<username>", methods=['GET'])
def get_user(username: str):
    if User.username_taken(username):
        user = User.by_username(username)
        return jsonify(user.json())

    return jsonify({"error": "User not found"}, status=404)


@app.route("/add_user", methods=['POST'])
def add_user():
    if request.get_json() is None:
        return jsonify({"error": "Invalid JSON"}, status=400)

    username = request.json.get('username', '')
    name = request.json.get('name', '')
    age = request.json.get('age', '')
    city = request.json.get('city', '')

    if username == "":
        return jsonify({"error": "Username is required"}, status=400)

    if User.username_taken(username):
        return jsonify({"error": "Username already exists"}, status=409)

    user = User(username, name, age, city)
    user.store()

    return jsonify({
        "message": "User added",
        "user": {
            "username": user.username,
            "name": user.name,
            "age": user.age,
            "city": user.city
        }
    })


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
