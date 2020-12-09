from db.config import db
from bson import json_util
import json

learningPaths = db.learningPaths

# Funcion para mostrar todas la rutas de aprendizaje
def showLearningPaths():
    data = learningPaths.find()
    result = []
    for r in data:
        result.append(r)

    return json.loads(json_util.dumps(result))

# Funcion para agregar una ruta de aprendizaje
def addLearningPaths(data: dict):
    #learningPaths.insert_one(data)
    learningPaths.insert(data, check_keys=False)

# Funcion para eliminar todas las rutas de aprendizaje
def deleteAllLearningPaths():
    learningPaths.delete_many({})

# Funcion para eliminar una ruta de aprendizaje por su id
def deleteLearningPathId(id: int):
    learningPaths.delete_one({'_id': id})

# Funcion para buscar una ruta de aprendizaje por su id
def searchLearningPathId(id: int):
    data = learningPaths.find_one({'_id': id})
    return data

def searchLearninfPathFilter(key: str, value: str):
    data = learningPaths.find({key: value})
    result = []

    for r in data:
        result.append(r)

    return json.loads(json_util.dumps(result))

def updateLearningPathId(id: int, data):
    learningPaths.find_one_and_update({'_id': id}, data)

def remplaceLearningPathId(id: int, data):
    learningPaths.find_one_and_replace({'_id': id}, data)

def searchLearningPathName(name: str):
    data = learningPaths.find_one({'learning Path': name})
    if data:
        return True
    else:
        return False

# Funcion para ver cuantas rutas de aprendizaje hay
def totalLearningPaths():
    return learningPaths.count_documents({})

