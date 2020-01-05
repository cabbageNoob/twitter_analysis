from flask import Blueprint

socialnet = Blueprint('socialnet', __name__)

from . import views
