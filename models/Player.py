from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    username_game1 = db.Column(db.String, unique=True)
    username_game2 = db.Column(db.String, unique=True)
    active = db.Column(db.Boolean)

    def __repr__(self):
        return '<Player %r>' % self.id
    
    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username_game1': self.username_game1,
            'username_game2': self.username_game2,
            'active': self.active,
        }