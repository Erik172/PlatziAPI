from db.config import db 
from bson import json_util
import json

posts = db.posts

# Funcion Para agregar Post
def addPost(data: dict):
    posts.insert_one(data)

# Funcion para mostrar todos los posts
def showPosts():
    data = posts.find()
    result = []
    for r in data:
        result.append(r)

    return json.loads(json_util.dumps(result))

# Funcion para buscar un post por su id
def searchPostId(id: int):
    data = posts.find_one({'_id': id})
    return data

def searchPostFilter(key: str, value):
    data = posts.find({key: value})
    result = []

    for r in data:
        result.append(r)

    return json.loads(json_util.dumps(result))

# Funcion para buscar un post por su titulo
def searchPostTitle(title: str):
    data = posts.find_one({'name': title})
    if data:
        return True
    else:
        return False

def deleteAllPosts():
    posts.delete_many({})

def totalPosts():
    return posts.count_documents({}) 