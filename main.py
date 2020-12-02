# Codigo Principal
from flask import Flask, render_template, request, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from config import auth
import models
import random
import os

from resource.courses import Courses, CoursesId
from resource.posts import Posts, PostsId

load_dotenv()

app = Flask(__name__)
api = Api(app)

@auth.verify_token
def verifyToken(token: str):
    if token == os.getenv('TOKEN'):
        return token

@app.route('/')
def home():
    cursosList = []
    postsList = []

    for _ in range(0, 4):
        cursosList.append(models.searchCourseId(random.randint(0, models.totalCourses())))

    for _ in range(0, 3):
        postsList.append(models.searchPostId(random.randint(0, models.totalPosts())),)

    context = {
        'cursos': cursosList,
        'posts': postsList
    }
    return render_template('index.html', **context)

api.add_resource(Courses, '/api/v1/courses')
api.add_resource(CoursesId, '/api/v1/courses/<int:id>')

api.add_resource(Posts, '/api/v1/posts')

if __name__ == "__main__":
    app.run(debug=True)