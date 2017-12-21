from flask import jsonify, Blueprint

from flask.ext.restful import Resource, Api

import models

class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}]})

class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

courses_api = Blueprint('resources.courses', __name__)
# treat this file with this name space and this path as being another app/thing: 
# a proxy to this module that serves as an app. kind of like a log.


api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='courses'
)
api.add_resource(
    Course,
    '/api/v1/courses/<int:id>',
    endpoint='course'
)
