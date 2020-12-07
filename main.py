# Codigo Principal
from flask import render_template
from flask_restful import Api
from dotenv import load_dotenv
from config import auth, app
import random
import os

from resource.courses import Courses, CoursesId, CoursesFilter
from resource.posts import Posts, PostsId, PostsFilter

# db
import db.courses as modelsCourses
import db.posts as modelsPosts

load_dotenv()

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
        cursosList.append(modelsCourses.searchCourseId(random.randint(0, modelsCourses.totalCourses())))

    for _ in range(0, 3):
        postsList.append(modelsPosts.searchPostId(random.randint(0, 10)))

    recommendedCourse = [
        modelsCourses.searchCourseId(356),
        modelsCourses.searchCourseId(347),
        modelsCourses.searchCourseId(551)
    ]

    context = {
        'cursos': cursosList,
        'recommendedCourse': recommendedCourse,
        'posts': postsList
    }
    return render_template('index.html', **context)

api.add_resource(Courses, '/api/v1/courses')
api.add_resource(CoursesId, '/api/v1/courses/<int:id>')
api.add_resource(CoursesFilter, '/api/v1/courses/<string:key>/<string:value>')

api.add_resource(Posts, '/api/v1/posts')
api.add_resource(PostsId, '/api/v1/posts/<int:id>')
api.add_resource(PostsFilter, '/api/v1/posts/<string:key>/<string:value>')

if __name__ == "__main__":
    app.run(debug=True)