from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')  # Carregar o arquivo config.py

db = SQLAlchemy(app)  # Inicializar o SQLAlchemy com o app

# Importar os modelos após inicializar o SQLAlchemy
from models.customer_model import Customer
