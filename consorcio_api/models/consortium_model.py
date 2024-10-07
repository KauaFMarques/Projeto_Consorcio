from consorcio_api import db

class Consortium(db.Model):
    __tablename__ = "consortium"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    valor_carro = db.Column(db.Float, nullable=False)
    prazo_meses = db.Column(db.Integer, nullable=False)
    taxa_administracao = db.Column(db.Float, nullable=False)
    parcelas_mensais = db.Column(db.Float, nullable=False)
    total_a_pagar = db.Column(db.Float, nullable=False)
