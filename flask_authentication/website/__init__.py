from flask import Flask
from dotenv import load_dotenv
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


# def create_app():
#     app = Flask(__name__)
#     load_dotenv()
#     app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#     app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
#     db.init_app(app)
def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from . import models

    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import User

        return User.query.get(int(id))

    return app


def create_database():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), DB_NAME)):
        db.create_all()
        print("Created Database!")
