from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import routes