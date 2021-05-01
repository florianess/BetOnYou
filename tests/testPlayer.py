import unittest
import json

from app import app, db
from models.Player import Player
class PlayerTest(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        self.db = db
        self.db.create_all()
    
    def test_get_all(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        response = self.app.get('/api/players/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.get_json()))
    
    def test_post(self):
        payload = json.dumps({
            "email": "john@doe.com",
            "username": "johndoe",
            "firstname": "john",
            "lastname": "doe"
        })
        response = self.app.post('/api/players/', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(201, response.status_code)

    def test_get_by_id(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        response = self.app.get('/api/players/1')
        player = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual("jojo", player['username'])

    def test_update(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        payload = json.dumps({
            "email": "doe@john.com",
            "username": "johndoe",
            "firstname": "john",
            "lastname": "doe"
        })
        response = self.app.put('/api/players/1', headers={"Content-Type": "application/json"}, data=payload)
        player = Player.query.filter_by(id=1).first()
        self.assertEqual(200, response.status_code)
        self.assertEqual("doe@john.com", player.email)

    def test_delete(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        response = self.app.delete('/api/players/1')
        players = Player.query.all()
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(players))
    
    def test_update_clash_royale(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        payload = json.dumps({
            "game_id": "GYUQQCLV",
        })
        response = self.app.put('/api/players/1/clash_royale', headers={"Content-Type": "application/json"}, data=payload)
        response_json = response.get_json()
        player = Player.query.filter_by(id=1).first()
        self.assertEqual(200, response.status_code)
        self.assertTrue('info' in response_json and 'matches' in response_json)
        self.assertEqual('GYUQQCLV', player.id_game1)

    def test_update_wrong_clash_royale(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        payload = json.dumps({
            "game_id": "toto",
        })
        response = self.app.put('/api/players/1/clash_royale', headers={"Content-Type": "application/json"}, data=payload)
        response_json = response.get_json()
        player = Player.query.filter_by(id=1).first()
        self.assertEqual(404, response.status_code)
        self.assertEqual(None, player.id_game1)

    def test_update_fortnite(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        payload = json.dumps({
            "username": "Ninja",
        })
        response = self.app.put('/api/players/1/fortnite', headers={"Content-Type": "application/json"}, data=payload)
        response_json = response.get_json()
        player = Player.query.filter_by(id=1).first()
        self.assertEqual(200, response.status_code)
        self.assertTrue('info' in response_json and 'matches' in response_json)
        self.assertEqual('Ninja', player.username_game2)

    def test_update_wrong_fortnite(self):
        new_player = Player(email="john@doe.com", username="jojo", firstname="john", lastname="doe")
        self.db.session.add(new_player)
        self.db.session.commit()
        payload = json.dumps({
            "username": "zregbeabsdfbrt",
        })
        response = self.app.put('/api/players/1/fortnite', headers={"Content-Type": "application/json"}, data=payload)
        response_json = response.get_json()
        player = Player.query.filter_by(id=1).first()
        self.assertEqual(404, response.status_code)
        self.assertEqual(None, player.username_game2)

    def tearDown(self):
        self.db.drop_all()