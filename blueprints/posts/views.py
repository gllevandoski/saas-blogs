from flask import Blueprint, request, jsonify
from blueprints.posts import database


posts = Blueprint("posts", __name__, url_prefix="/posts")


@posts.get("/<post_id>")
def get_post(post_id):
    query = database.get_post(post_id)
    return jsonify(str(query))


@posts.get("/")
def get_posts():
    query = database.get_posts()
    return jsonify(str(query))


@posts.post("/")
def create_post():
    title = request.json["title"]
    content = request.json["content"]
    query = database.create_post(title, content)
    return jsonify(str(query))


@posts.put("/<post_id>")
def update_post(post_id):
    title = request.json["title"]
    content = request.json["content"]
    query = database.update_post(post_id, title, content)
    return jsonify(str(query))


@posts.delete("/<post_id>")
def delete_post(post_id):
    query = database.delete_post(post_id)
    return jsonify(str(query))
