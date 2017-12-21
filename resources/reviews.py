from flask import jsonify, Blueprint

from flask.ext.restful import Resource, Api

import models

class ReviewList(Resource):
    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})

reviews_api = Blueprint('resouces.reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/api/v1/reviews',
    endpoint='reviews'
)
api.add_resource(
    Review,
    '/api/v1/reviews/<int:id>',
    endpoint='review'
)