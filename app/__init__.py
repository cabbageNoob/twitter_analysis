from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
# from app.models import User, Role

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view='auth.login'

def create_app(config_name):
    print(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .socialnet import socialnet as socialnet_blueprint
    app.register_blueprint(socialnet_blueprint)

    from .emotion_analyses import emotion_analyses as emotion_analyses_blueprint
    app.register_blueprint(emotion_analyses_blueprint)

    return app
