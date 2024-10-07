from consorcio_api import db

class Customer(db.Model):
    __tablename__="customer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    renda_mensal = db.Column(db.Float, nullable=False)
    historico_credito = db.Column(db.String(50), nullable=False)
    compromissos = db.Column(db.Float, nullable=False)