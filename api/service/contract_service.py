from models.contract_model import Contract
from api import db

def cadastrar_contrato(contrato):
    db.session.add(contrato)
    db.session.commit()
    return contrato

def listar_contrato_id(id):
    return Contract.query.filter_by(id=id).first()

def listar_contratos():
    return Contract.query.all()

def atualizar_contrato(contrato_bd, contrato_novo):
    contrato_bd.customer = contrato_novo.customer
    contrato_bd.consortium = contrato_novo.consortium
    contrato_bd.aprovado = contrato_novo.aprovado
    db.session.commit()

def remover_contrato(contrato):
    db.session.delete(contrato)
    db.session.commit()