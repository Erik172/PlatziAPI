# Archivo para manejar todo lo de la base de datos
from pymongo import MongoClient
from bson import json_util
import json
import os

# Conectarse a la base de datos MongoDB de manera local
#client = MongoClient('localhost', 27017)

# Conectarse a la base de datos en producion
client = MongoClient(os.environ["MONGO_DB"])

db = client.platzi # Base de datos nombrada como platzi
courses = db.courses # Colecion de cursos
posts = db.posts # Colecion de posts (Blog de Platzi)
users = db.users # Colecion de usuarios (De la API)

### Cursos ###

# Funcion para buscar y mostrar todos los cursos
def showCourses():
    data = courses.find()
    result = []
    for r in data:
        result.append(r)

    # Retorna un archivo json con todos los cursos
    return json.loads(json_util.dumps(result))

# Funcion para agregar un curso
def addCourse(data: dict):
    courses.insert_one(data)

# Funcion para !ELIMINAR TODOS LOS CURSOS!
def deleteAllCourses():
    courses.delete_many({})

# Funcion para buscar un curso por su _id
def searchCourseId(id: int):
    data = courses.find_one({"_id": id})
    return data

# Funcion para buscar un curso por su nombre
def searchCourseName(name: str):
    data = courses.find_one({'course': name})
    if data:
        return True

    else:
        return False

# Funcion para modificar un curso por su _id
def modifiedCourseId(id: int, data: dict):
    courses.find_and_modify({"_id": id}, data)

# Funcion para eliminar un curso por su _id
def deleteCourseId(id: int):
    courses.find_one_and_delete({"_id": id})

def totalCourses():
    return courses.count_documents({})

### Posts ###

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

# Funcion para buscar un post por su titulo
def searchPostTitle(title: str):
    data = posts.find_one({'name': title})
    if data:
        return True
    else:
        return False

def totalPosts():
    return posts.count_documents({}) 
