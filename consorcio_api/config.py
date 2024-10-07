DEBUG = True

USERNAME = 'root'
PASSWORD = 'mk875'
SERVER = 'localhost'
DB = 'consorcio_db'

# String de conexão para PostgreSQL
SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativar por motivos de performance
SECRET_KEY = "aplicacao_flask"
