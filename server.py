from flask import Flask 
import models
from resources.courses import courses_api
from resources.reviews import reviews_api

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api)

DEBUG = True
HOST = '0.0.0.0'
PORT = 5000


@app.route('/')
def hello_word():
  return 'hello world'

if __name__ == '__main__':
  models.connect_to_db(app)
  app.run(debug=DEBUG, host=HOST, port=PORT)