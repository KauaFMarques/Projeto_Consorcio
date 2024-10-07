from ..models import customer_model
from consorcio_api import db

def cadastrar_cliente(cliente):
    cliente_bd = customer_model.Customer(
        nome=cliente.nome,
        email=cliente.email,
        senha=cliente.senha,
        api_key=cliente.api_key,
        address=cliente.address,
        cpf=cliente.cpf
    )
    db.session.add(cliente_bd)
    db.session.commit()
    return cliente_bd

def listar_clientes():
    return customer_model.Customer.query.all()

def listar_cliente_id(id):
    return customer_model.Customer.query.filter_by(id=id).first()

def atualiza_cliente(cliente_anterior, cliente_novo):
    cliente_anterior.nome = cliente_novo.nome
    cliente_anterior.email = cliente_novo.email
    cliente_anterior.senha = cliente_novo.senha
    cliente_anterior.api_key = cliente_novo.api_key
    cliente_anterior.address = cliente_novo.address
    cliente_anterior.cpf = cliente_novo.cpf
    db.session.commit()

def remover_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()
