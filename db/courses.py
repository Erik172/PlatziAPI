from db.config import db
from bson import json_util
import json

courses = db.courses

# Funcion para buscar y mostrar todos los cursos
def showCourses():
    data = courses.find()
    result = []
    for r in data:
        result.append(r)

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
 
def updateCourseId(id: int, data: dict):
    courses.find_one_and_update({'_id': id}, data)

# Funcion para remplasar un curso por su id
def remplaceCourseId(id: int, data: dict):
    courses.find_one_and_replace({'_id': id}, data)

def searchCourseFilter(key: str, value):
    data = courses.find({key: value})
    result = []
    for r in data:
        result.append(r)

    return json.loads(json_util.dumps(result))

# Funcion para buscar un curso por su nombre
def searchCourseName(name: str):
    data = courses.find_one({'course': name})
    if data:
        return True

    else:
        return False

# Funcion para eliminar un curso por su _id
def deleteCourseId(id: int):
    courses.find_one_and_delete({"_id": id})

def totalCourses():
    return courses.count_documents({})