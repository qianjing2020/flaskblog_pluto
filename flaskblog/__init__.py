from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

""" Do this in python to get a 16-digit secrete key
import secrets
secrets.token_hex(16)
"""
app.config['SECRET_KEY'] = 'fbf66f6ad2c5cf369684851f8ffa51da'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['DEBUG'] = os.getenv(DEBUG_MODE)
#app.config['ENV'] = os.getenv(FLASK_ENV)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_messae_category = 'info'

from flaskblog import routes
