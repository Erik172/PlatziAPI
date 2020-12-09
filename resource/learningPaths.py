from flask_restful import Resource, request
import db.learningPaths as modelsLearningPaths
from config import auth

class LearningPath(Resource):
    def get(self):
        data = modelsLearningPaths.showLearningPaths()
        return data

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        modelsLearningPaths.addLearningPaths(data)
        return 201, data

    @auth.login_required
    def delete(self):
        modelsLearningPaths.deleteAllLearningPaths()
        return 201

class LearningPathId(Resource):
    def get(self, id: int):
        data = modelsLearningPaths.searchLearningPathId(id)
        return data

    @auth.login_required
    def put(self, id: int):
        data = request.get_json(force=True)
        if data['_id']:
            modelsLearningPaths.remplaceLearningPathId(id, data)

        else:
            modelsLearningPaths.updateLearningPathId(id, data)

        return data, 201

    @auth.login_required
    def delete(self, id: int):
        modelsLearningPaths.deleteLearningPathId(id)
        return 201

class LearningPathFilter(Resource):
    def get(self, key: str, value: str):
        data = modelsLearningPaths.searchLearninfPathFilter(key, value)
        return data