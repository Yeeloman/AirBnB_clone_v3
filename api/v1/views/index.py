#!/usr/bin/python3
"""Create a Route `/status` on the object app_views."""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def jsonstatus():
    """the return ok status"""
    return jsonify(status='OK')


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def getstats():
    """endpoint that retrives the number of each obcts by type"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    obj_count = {}
    for i in range(len(classes)):
        obj_count[names[i]] = storage.count(classes[i])

    return jsonify(obj_count)
