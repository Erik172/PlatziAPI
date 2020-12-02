from flask import request
from flask_restful import Resource
from config import auth
import models

class Posts(Resource):
    def get(self):
        posts = models.showPosts()
        return posts

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        models.addPost(data)

        return data, 201

class PostsId(Resource):
    def get(self, id: int):
        post = models.searchPostId(id)
        return post