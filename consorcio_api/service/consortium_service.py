from ..models import consortium_model
from consorcio_api import db

def cadastrar_consorcio(consorcio):
    consorcio_bd = consortium_model.Consortium(
        nome=consorcio.nome,
        descricao=consorcio.descricao,
        data_publicacao=consorcio.data_publicacao,
        valor_total=consorcio.valor_total,
        numero_participantes=consorcio.numero_participantes
    )
    db.session.add(consorcio_bd)
    db.session.commit()
    return consorcio_bd

def listar_consorcios():
    return consortium_model.Consortium.query.all()

def listar_consorcio_id(id):
    return consortium_model.Consortium.query.filter_by(id=id).first()

def atualiza_consorcio(consorcio_anterior, consorcio_novo):
    consorcio_anterior.nome = consorcio_novo.nome
    consorcio_anterior.descricao = consorcio_novo.descricao
    consorcio_anterior.data_publicacao = consorcio_novo.data_publicacao
    consorcio_anterior.valor_total = consorcio_novo.valor_total
    consorcio_anterior.numero_participantes = consorcio_novo.numero_participantes
    db.session.commit()

def remover_consorcio(consorcio):
    db.session.delete(consorcio)
    db.session.commit()
