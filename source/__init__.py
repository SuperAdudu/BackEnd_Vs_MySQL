from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.abspath('media')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/cosplay'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from source.main.controllers import register_routes
    register_routes(app)
    
    return app

