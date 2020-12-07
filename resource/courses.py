from flask import request
from flask_restful import Resource
from config import auth

import db.courses as models

class Courses(Resource):
    # Funcion para mostrar todos los cursos
    def get(self):
        courses = models.showCourses()
        info = models.totalCourses()
        return courses
    
    # Funcion para agregar cursos
    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        models.addCourse(data)

        return data, 201

    # Funcion para eliminar !TODOS LOS CURSOS!
    @auth.login_required
    def delete(self):
        models.deleteAllCourses()

        return 201

class CoursesId(Resource):
    # Funcion para buscar un curso por su _id
    def get(self, id: int):
        course = models.searchCourseId(id)
        return course

    # Funcion para editar un curso por su _id
    @auth.login_required
    def put(self, id: int):
        data = request.get_json(force=True)
        models.modifiedCourseId(id, data)

        return data, 201

    # Funcion para Eliminar un curso por su _id
    @auth.login_required
    def delete(self, id: int):
        models.deleteCourseId(id)

        return 201

class CoursesFilter(Resource):
    def get(self, key: str, value):
        data = models.searchCourseFilter(key, value)
        return data