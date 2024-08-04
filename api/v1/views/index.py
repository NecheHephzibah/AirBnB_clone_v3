#!/usr/bin/python3
"""
Create flask app, instance of Flask.
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """

    """

    resp = {'status': "OK"}
    return jsonify(resp)
