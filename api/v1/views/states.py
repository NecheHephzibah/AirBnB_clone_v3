#!/usr/bin/python3
"""
Creates a new view for State objs that handles all default API .
"""
from flask import jsonify, abort, request
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/states', strict_slashes=False)
def get_all_states():
    """
    Gets all state objects
    """
    states = storage.all(State).values()
    states_list = [state.to_dict() for state in states]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """Gets all state objects id"""
    state = storage.get(State, state_id)

    if state:
        return jsonify(state.to_dict())
    else:
        return abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)  # noqa
def delete_state(state_id):
    """Deletes a state object"""
    state = storage.get(State, state_id)

    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a new state object"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')

    keys = request.get_json()
    if 'name' not in keys:
        abort(400, 'Missing name')

    state = State(**keys)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update existing state object"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')

    state = storage.get(State, state_id)

    if state:
        if not request.get_json():
            return abort(400, 'Not a JSON')
        retrieve_data = request.get_json()
        ignore_attr = ['id', 'created_at', 'updated_at']

        for key, value in retrieve_data.items():
            if key not in ignore_attr:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200
    else:
        return abort(404)
