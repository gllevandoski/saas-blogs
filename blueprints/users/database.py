from bson import ObjectId
from database import database
collection = database["users"]


def get_user(user_id):
    query = collection.find_one({"_id": ObjectId(user_id)})

    if query is None:
        return f"User with id {user_id} not found"

    return query


def get_users():
    query = collection.find()
    return [each for each in query]


def create_user(title, content):
    query = collection.insert_one({"title": title, "content": content})
    return query


def update_user(user_id, title, content):
    query = collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"title": title, "content": content}})
    return query


def delete_user(user_id):
    query = collection.delete_one({"_id": ObjectId(user_id)})

    if query.deleted_count == 0:
        return f"User with id {user_id} not found"

    return query
