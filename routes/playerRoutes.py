from flask import Blueprint, jsonify, request, Response
from controllers import playerController

playerRoutes = Blueprint('playerRoutes', __name__)

@playerRoutes.route('/', methods=['GET'])
def getAll():
    return jsonify(playerController.get_all())

@playerRoutes.route('/', methods=['POST'])
def add():
    data = request.get_json()
    playerController.add(data['email'], data['username'], data['firstname'], data['lastname'])
    response = Response('Player added', 201)
    return response

@playerRoutes.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return jsonify(playerController.get_by_id(id))

@playerRoutes.route('/<int:id>', methods=['DELETE'])
def remove(id):
    playerController.delete(id)
    response = Response("Player deleted", 200)
    return response

@playerRoutes.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    playerController.update(id, data['email'], data['username'], data['firstname'], data['lastname'])
    response = Response("Player updated", 200)
    return response

@playerRoutes.route('/<int:id>/clash_royale', methods=['PUT'])
def update_player_game_1(id):
    data = request.get_json()
    player_info = playerController.update_clash_royale(id, data['game_id'])
    if (player_info is None):
        response = Response("Game Id invalid", 404)
        return response
    return jsonify(player_info)

@playerRoutes.route('/<int:id>/fortnite', methods=['PUT'])
def update_player_game_2(id):
    data = request.get_json()
    player_info = playerController.update_fortnite(id, data['username'])
    if (player_info is None):
        response = Response("Username invalid", 404)
        return response
    return jsonify(player_info)