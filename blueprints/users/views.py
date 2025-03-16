from flask import Blueprint, request, jsonify
from blueprints.users import database


users = Blueprint("users", __name__, url_prefix="/users")


@users.get("/<user_id>")
def get_user(user_id):
    query = database.get_user(user_id)
    return jsonify(str(query))


@users.get("/")
def get_users():
    query = database.get_users()
    return jsonify(str(query))


@users.post("/")
def create_user():
    username = request.json["username"]
    password = request.json["password"]
    query = database.create_user(username, password)
    return jsonify(str(query))


@users.put("/<user_id>")
def update_user(user_id):
    username = request.json["username"]
    password = request.json["password"]
    query = database.update_user(user_id, username, password)
    return jsonify(str(query))


@users.delete("/<user_id>")
def delete_user(user_id):
    query = database.delete_user(user_id)
    return jsonify(str(query))
