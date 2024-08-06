#!/usr/bin/python3
"""
Create Flask app blueprint, instance of Flask.
"""
from flask import Blueprint
from api.v1.views import index
from api.v1.views import states

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
