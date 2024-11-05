import os
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager,
    )   

from dotenv import  load_dotenv
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') # chequear a donde manda la informacion con respecto a la base de datos no encontrada de celulares.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

from services.paises_service import PaisService
from celulares import  *
from forms import PaisForm
from repositories.paises_repository import PaisRepository

load_dotenv()

from views import register_bp
register_bp(app)


