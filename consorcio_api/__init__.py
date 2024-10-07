from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

# Importe suas views e models após a definição do app
from .views import customer_views, contract_views, consortium_views
from .models import customer_model, consortium_model, contract_model
