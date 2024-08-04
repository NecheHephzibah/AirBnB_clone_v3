#!/usr/bin/python3
"""
Create flask app, instance of Flask.
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def api_status():
    """
    creates api for route status, it will return a json response.
    """

    resp = {'status': "OK"}
    return jsonify(resp)

@app_views.route('/stats')
def retrieve_stats():
    """
    creates api for route stats
    """

    stats = {
         'amenities': storage.count('Amenity'),
         'cities': storage.count('City'),
         'places': storage.count('Place'),
         'reviews': storage.count('Review'),
         'states': storage.count('State'),
         'users': storage.count('User'),
    }
    return jsonify(stats)
