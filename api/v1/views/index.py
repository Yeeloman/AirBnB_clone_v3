#!/usr/bin/python3
"""Create a Route `/status` on the object app_views."""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def jsonstatus():
    """the return ok status"""
    return jsonify(status='OK')


@app_views.route('/api/v1/stats', methods=['GET'])
def getstats():
    """endpoint that retrives the number of each obcts by type"""
    dicreturn = {"amenities": storage.count('amenities'),
                 "cities": storage.count('cities'),
                 "places": storage.count('places'),
                 "reviews": storage.count('reviews'),
                 "states": storage.count('states'),
                 "users": storage.count('users')}
    return jsonify(dicreturn)
