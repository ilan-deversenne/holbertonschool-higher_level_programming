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
    users = {}

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
        User.users[self.username] = self.json()

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
        print(User.users)
        return username in User.users

    @staticmethod
    def by_username(username: str):
        """
        Get a stored user by his username

        :param username: Username
        :type username: str
        """
        return User.users[username]


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
    for key, data in User.users.items():
        result.append(data['username'])

    return jsonify(result)


@app.route("/users/<username>", methods=['GET'])
def get_user(username: str):
    """
    [GET] /users/<username> route

    :param username: Username
    :type username: str
    """

    if User.username_taken(username):
        user = User.by_username(username)
        return jsonify(user)

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

    if User.username_taken(username):
        return jsonify({"error": "Username already exists"}), 409

    user = User(username, name, age, city)
    user.store()

    return jsonify({
        "message": "User added",
        "user": user.json()
    })


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
