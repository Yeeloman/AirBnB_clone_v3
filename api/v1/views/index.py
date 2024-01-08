#!/usr/bin/python3
"""Create a Route `/status` on the object app_views."""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methode=['GET'])
def jsonstatus():
    """the return ok status"""
    return jsonify(status='OK')
