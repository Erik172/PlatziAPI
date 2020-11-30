# Codigo Principal
from flask import Flask, request, render_template
from flask_restful import Resource, Api, abort
import models
import random
import ETL
import os

app = Flask(__name__)
api = Api(app)

### CURSOS ###

# Ruta Principal
@app.route('/')
def home():
    cursoslist = [
        models.searchCourseId(random.randint(0, models.totalCourses())),
        models.searchCourseId(random.randint(0, models.totalCourses())),
        models.searchCourseId(random.randint(0, models.totalCourses())),
        models.searchCourseId(random.randint(0, models.totalCourses())),
        # models.searchCourseId(random.randint(0, models.totalCourses())),
        # models.searchCourseId(random.randint(0, models.totalCourses()))
    ]
    context = {
        'cursos': cursoslist
    }
    return render_template('index.html', **context)

@app.route('/api/courses/reload')
def reloadCourses():
    ETL.automaticSpiderPlatzi()

@app.route('/api/courses/reload')
def reloadPosts():
    ETL.automaticSpiderBlog()

class Courses(Resource):
    # Funcion para mostrar todos los cursos
    def get(self):
        courses = models.showCourses()
        return courses

    # Funcion para agregar cursos
    def post(self):
        data = request.get_json(force=True)
        models.addCourse(data)

        return data, 201

    # Funcion para eliminar !TODOS LOS CURSOS!
    def delete(self):
        models.deleteAllCourses()

        return 201

class CoursesId(Resource):
    # Funcion para buscar un curso por su _id
    def get(self, id: int):
        course = models.searchCourseId(id)
        return course

    # Funcion para editar un curso por su _id
    def put(self, id: int):
        data = request.get_json(force=True)
        models.modifiedCourseId(id, data)

        return data, 201

    # Funcion para Eliminar un curso por su _id
    def delete(self, id: int):
        models.deleteCourseId(id)

        return 201

### POSTS ###

class Posts(Resource):
    def get(self):
        posts = models.showPosts()
        return posts

class PostsId(Resource):
    def get(self, id: int):
        post = models.searchPostId(id)
        return post

### PROFILE ###

class ProfileUsername(Resource):
    def get(self, username: str):
        request.get(f'https://platzi.com/@{username}')

# Ruta para todos los cursos
api.add_resource(Courses, '/api/courses')

# Ruta para las funciones dentro de la clase CoursesId
api.add_resource(CoursesId, '/api/courses/<int:id>')

# Ruta para las funciones de posts
api.add_resource(Posts, '/api/posts')

# Ruta para obtener los datos del usuario platzi
api.add_resource(ProfileUsername, '/api/user/<string:username>')

if __name__ == "__main__":
    app.run(debug=True)