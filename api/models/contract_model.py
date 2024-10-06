from api import db
from .customer_model import Customer
from .consortium_model import Consortium

class Contract(db.Model):
    __tablename__ = "contract"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    consortium_id = db.Column(db.Integer, db.ForeignKey('consortium.id'), nullable=False)
    aprovado = db.Column(db.Boolean, nullable=False)

    customer = db.relationship('Customer', backref=db.backref('contracts', lazy=True))
    consortium = db.relationship('Consortium', backref=db.backref('contracts', lazy=True))