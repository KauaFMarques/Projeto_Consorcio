from flask_restful import Resource
from consorcio_api import api
from ..schemes import consorcio_schema
from flask import request, make_response, jsonify
from ..entidades import consorcio
from ..service import consorcio_service
from ..views import paginate
from ..models.consortium_model import Consorcio
from flask_jwt_extended import jwt_required

class ConsorcioList(Resource):
    @jwt_required()
    def get(self):
        cs = consorcio_schema.ConsorcioSchema(many=True)
        return paginate(Consorcio, cs)

    @jwt_required()
    def post(self):
        cs = consorcio_schema.ConsorcioSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            novo_consorcio = consorcio.Consorcio(nome=nome, descricao=descricao)
            resultado = consorcio_service.cadastrar_consorcio(novo_consorcio)
            x = cs.jsonify(resultado)
            return make_response(x, 201)

class ConsorcioDetail(Resource):
    @jwt_required()
    def get(self, id):
        consorcio = consorcio_service.listar_consorcio_id(id)
        if consorcio is None:
            return make_response(jsonify("Consórcio não foi encontrado"), 404)
        cs = consorcio_schema.ConsorcioSchema()
        return make_response(cs.jsonify(consorcio), 200)

    @jwt_required()
    def put(self, id):
        consorcio_bd = consorcio_service.listar_consorcio_id(id)
        if consorcio_bd is None:
            return make_response(jsonify("Consórcio não foi encontrado"), 404)
        cs = consorcio_schema.ConsorcioSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            novo_consorcio = consorcio.Consorcio(nome=nome, descricao=descricao)
            consorcio_service.atualiza_consorcio(consorcio_bd, novo_consorcio)
            consorcio_atualizado = consorcio_service.listar_consorcio_id(id)
            return make_response(cs.jsonify(consorcio_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        consorcio_bd = consorcio_service.listar_consorcio_id(id)
        if consorcio_bd is None:
            return make_response(jsonify("Consórcio não encontrado"), 404)
        consorcio_service.remove_consorcio(consorcio_bd)
        return make_response('Consórcio excluído com sucesso', 204)

api.add_resource(ConsorcioList, '/consorcios')
api.add_resource(ConsorcioDetail, '/consorcios/<int:id>')
