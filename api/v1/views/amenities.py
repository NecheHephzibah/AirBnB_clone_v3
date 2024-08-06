#!/usr/bin/python3
"""
Creates a new view for State objs that handles all default API .
"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
