from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Initializing application
app = Flask(__name__)


#Initializing flask extensions
db = SQLAlchemy()
db.init_app(app)

from app import views