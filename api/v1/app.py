#!/usr/bin/python3
"""
reate Flask app; and register the blueprint app_views to Flask instance app.
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(args):
    """
    Removes the current SQLAlchemy Session object after each request.
    """
    storage.close()


if __name__ == '__main__':
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)