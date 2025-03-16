from bson import ObjectId
from database import database
collection = database["posts"]


def get_post(post_id):
    query = collection.find_one({"_id": ObjectId(post_id)})

    if query is None:
        return f"Post with id {post_id} not found"

    return query


def get_posts():
    query = collection.find()
    return [each for each in query]


def create_post(title, content):
    query = collection.insert_one({"title": title, "content": content})
    return query


def update_post(post_id, title, content):
    query = collection.update_one({"_id": ObjectId(post_id)}, {"$set": {"title": title, "content": content}})
    return query


def delete_post(post_id):
    query = collection.delete_one({"_id": ObjectId(post_id)})

    if query.deleted_count == 0:
        return f"Post with id {post_id} not found"

    return query
