from flask import Blueprint
from . import forms

auth = Blueprint('auth',__name__)


from . import views