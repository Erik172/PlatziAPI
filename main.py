# Codigo Principal
from flask import render_template, request, jsonify
from flask import json
from flask_restful import Api
from dotenv import load_dotenv
from scrapinghub.legacy import Job
from config import auth, app
import models
import random
import ETL
import os

from resource.courses import Courses, CoursesId, CoursesFilter
from resource.posts import Posts, PostsId, PostsFilter

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
        cursosList.append(models.searchCourseId(random.randint(0, models.totalCourses())))

    for _ in range(0, 3):
        postsList.append(models.searchPostId(random.randint(0, models.totalPosts())))

    context = {
        'cursos': cursosList,
        'posts': postsList
    }
    return render_template('index.html', **context)

@auth.login_required
@app.route('/api/v1/start-job-platzi')
def startScrpingPlatzi():
    try:
        ETL.initSpiderPlatzi()
        return "Job Iniciado"
    except:
        return 'El trabajo Ya Inicio'

@auth.login_required
@app.route('/api/v1/filter-platzi-courses')
def filterDataCourses():
    with open('jobs/platzi.log') as fr:
        file = fr.read()
        ETL.dataSpiderPlatziFilterCourses(int(file))
        file = int(file) + 1
        fr.close()
        with open('jobs/platzi.log', 'w')as f:
            f.write(str(file))
            f.close()

            return "Listo"

api.add_resource(Courses, '/api/v1/courses')
api.add_resource(CoursesId, '/api/v1/courses/<int:id>')
api.add_resource(CoursesFilter, '/api/v1/courses/<string:key>/<string:value>')

api.add_resource(Posts, '/api/v1/posts')
api.add_resource(PostsId, '/api/v1/posts/<int:id>')
api.add_resource(PostsFilter, '/api/v1/posts/<string:key>/<string:value>')

if __name__ == "__main__":
    app.run(debug=True)