from app import app

from routes.playerRoutes import playerRoutes

app.register_blueprint(playerRoutes, url_prefix='/api/players')