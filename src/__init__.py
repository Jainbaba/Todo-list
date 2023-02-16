from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


'''
Initializes of Flask and CORS.
'''
app = Flask(__name__)
CORS(app)

'''
Initializes and Configuration of SQLAlchemy for Database connection.
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

'''Importing here due to a circular import'''
from src import routes
from src import models
from src import errorhandlers
'''
Registering Blueprint for Tasks and errors
'''
app.register_blueprint(routes.tasks, url_prefix='/api/v1')
app.register_blueprint(errorhandlers.errors)

with app.app_context():
    db.create_all()