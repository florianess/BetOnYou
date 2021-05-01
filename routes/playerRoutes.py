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