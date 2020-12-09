# Codigo Principal
from flask import render_template, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from config import auth, app
import random
import os

from resource.courses import Courses, CoursesId, CoursesFilter
from resource.learningPaths import LearningPath, LearningPathId, LearningPathFilter
from resource.posts import Posts, PostsId, PostsFilter

# db
import db.courses as modelsCourses
import db.learningPaths as modelsLearningPaths
import db.posts as modelsPosts

load_dotenv()

api = Api(app)

@auth.verify_token
def verifyToken(token: str):
    if token == os.getenv('TOKEN'):
        return token

@app.errorhandler(404)
def error404(e):
    return jsonify({'error': {'Page not found, Error': 404}})

@app.errorhandler(500)
def error500():
    return render_template('errors/500.html')

@app.route('/')
def home():
    cursosList = []
    learningPathList = []
    postsList = []

    for _ in range(0, 4):
        cursosList.append(modelsCourses.searchCourseId(random.randint(0, modelsCourses.totalCourses())))

    for _ in range(0, 3):
        postsList.append(modelsPosts.searchPostId(random.randint(0, 10)))

    for _ in range(0, 4):
        learningPathList.append(modelsLearningPaths.searchLearningPathId(random.randint(0, modelsLearningPaths.totalLearningPaths())))

    recommendedCourse = [
        modelsCourses.searchCourseId(355),
        modelsCourses.searchCourseId(563),
        modelsCourses.searchCourseId(352)
    ]

    context = {
        'cursos': cursosList,
        'learningPaths': learningPathList,
        'recommendedCourse': recommendedCourse,
        'posts': postsList
    }
    return render_template('index.html', **context)

api.add_resource(Courses, '/api/v1/courses')
api.add_resource(CoursesId, '/api/v1/courses/<int:id>')
api.add_resource(CoursesFilter, '/api/v1/courses/<string:key>/<string:value>')

api.add_resource(LearningPath, '/api/v1/learningPaths')
api.add_resource(LearningPathId, '/api/v1/learningPaths/<int:id>')
api.add_resource(LearningPathFilter, '/api/v1/learningPaths/<string:key>/<string:value>')

api.add_resource(Posts, '/api/v1/posts')
api.add_resource(PostsId, '/api/v1/posts/<int:id>')
api.add_resource(PostsFilter, '/api/v1/posts/<string:key>/<string:value>')

if __name__ == "__main__":
    app.run(debug=True)