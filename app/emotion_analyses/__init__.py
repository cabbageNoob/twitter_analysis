from flask import Blueprint

emotion_analyses = Blueprint('emotion_analyses', __name__)

from . import views
