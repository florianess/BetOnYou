from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Bet On You Florian"
    },
)

app.register_blueprint(swaggerui_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import routes