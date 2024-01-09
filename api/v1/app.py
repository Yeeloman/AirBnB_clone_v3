#!/usr/bin/python3
"""
reate Flask app; and register the blueprint app_views to Flask instance app.
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(args):
    """
    Removes the current SQLAlchemy Session object after each request.
    """
    storage.close()


@app.errorhandler(404)
def not_found_page(err):
    return jsonify(error="Not found"), 404


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
