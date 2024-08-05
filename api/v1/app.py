#!/usr/bin/python3
"""
Create an app, instance of Flask.
"""
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_engine(exception):
    """
    Ends current session
    """
    storage.close()


@app.errorhandler(404)
def error_not_found(error):
    """
     create a handler for 404 errors that returns a
     JSON-formatted 404 status code response.
    """
    resp = {"error": "Not Found"}
    return jsonify(resp), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
