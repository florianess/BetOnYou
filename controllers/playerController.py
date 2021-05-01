from app import db
from models.Player import Player

def get_all():
    return [Player.json(player) for player in Player.query.all()]

def add(_email, _username, _firstname, _lastname):
    new_player = Player(email=_email, username=_username, firstname=_firstname, lastname=_lastname)
    db.session.add(new_player)
    db.session.commit()

def get_by_id(_id):
    return Player.json(Player.query.filter_by(id=_id).first())

def delete(_id):
    Player.query.filter_by(id=_id).delete()
    db.session.commit()

def update(_id, _email, _username, _firstname, _lastname):
    player_to_update = Player.query.filter_by(id=_id).first()
    player_to_update.email = _email
    player_to_update.username = _username
    player_to_update.firstname = _firstname
    player_to_update.lastname = _lastname
    db.session.commit()