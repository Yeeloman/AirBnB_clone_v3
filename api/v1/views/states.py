#!/usr/bin/python3
"""state"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, request, jsonify


@app_views.route("/api/v1/states", strict_slashes=False, methods=["GET"])
@app_views.route(
    '/api/v1/states/<state_id>',
    strict_slashes=False,
    methods=['GET']
)
def state_page(state=None):
    """show all states or with a specific id"""
    ls_state = []
    if not state:
        objs = storage.all(State).values()
        for value in objs:
            ls_state.append(value.to_dict())
        return jsonify(ls_state)
    else:
        id_state = storage.get(State, state)
        if not state:
            abort(404)
        return jsonify(id_state.to_dict())


@app_views.route(
    '/api/v1/states/<state_id>',
    strict_slashes=False,
    methods=['DELETE']
)
def delete_state(state_id):
    """delete a state based on its id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route(
    '/api/v1/states/',
    strict_slashes=False,
    methods=['POST']
)
def create_state():
    """create a new state"""
    http_header = request.get_json(force=True, silent=True)
    if not http_header:
        abort(400, "Not a JSON")
    if "name" not in http_header:
        abort(400, "Missing name")
    new_state = State(**http_header)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route(
    '/api/v1/states/<state_id>',
    strict_slashes=False,
    methods=['PUT']
)
def update_state(state_id):
    """update a state based on its id"""
    updated_state = storage.get(State, state_id)
    if not updated_state:
        abort(404)
    http_header = request.get_json(force=True, silent=True)
    if not http_header:
        abort(400, "Not a JSON")
    updated_state.name = http_header.get("name", updated_state.name)
    updated_state.save()
    return jsonify(updated_state.to_dict()), 200
