import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy() 

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return 'Course {}'.format(self.title)

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return 'Review {}'.format(self.rating)

def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///courses'
    db = SQLAlchemy(app)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all(app=app)
    