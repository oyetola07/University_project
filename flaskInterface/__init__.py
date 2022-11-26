from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager 



app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

UPLOAD_FOLDER = '/storage'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

app.config['SECRET_KEY']='b8b9f3d03b7514b9e92d628fe4a5b4da'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'storage/files'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




db =  SQLAlchemy(app)

bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'

from flaskInterface import routes