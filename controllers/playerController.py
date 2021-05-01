import json

from app import db
from models.Player import Player
from services import ClashRoyale, Fortnite

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

def update_clash_royale(_id, battletag):
    player_info = ClashRoyale.get_player_info(battletag)
    if (player_info is None):
        return
    player_to_update = Player.query.filter_by(id=_id).first()
    player_to_update.id_game1 = battletag
    player_to_update.username_game1 = player_info['name']
    player_to_update.stats_game1 = json.dumps(player_info)
    db.session.commit()
    player_matches = ClashRoyale.get_player_matches(battletag)
    return {'info': player_info, 'matches': player_matches}

def update_fortnite(_id, username):
    player_info = Fortnite.get_player_info(username)
    if (player_info is None):
        return
    player_to_update = Player.query.filter_by(id=_id).first()
    player_to_update.id_game2 = player_info['id']
    player_to_update.username_game2 = player_info['name']
    player_to_update.stats_game2 = json.dumps(player_info['global_stats'])
    db.session.commit()
    player_matches = Fortnite.get_player_matches(player_info['id'])
    return {'info': player_info, 'matches': player_matches}

def get_stats(_id):
    return Player.stats(Player.query.filter_by(id=_id).first())

def get_stats_game(_id, _game):
    all_stats = get_stats(_id)
    return all_stats[_game]