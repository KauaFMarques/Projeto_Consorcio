from flask_restful import Resource
from consorcio_api import api
from ..schemes import contrato_schema
from flask import request, make_response, jsonify
from ..entidades import contrato
from ..services import contrato_service
from ..models.contrato_model import Contrato
from flask_jwt_extended import jwt_required

class ContratoList(Resource):
    @jwt_required()
    def get(self):
        cs = contrato_schema.ContratoSchema(many=True)
        return paginate(Contrato, cs)

    @jwt_required()
    def post(self):
        cs = contrato_schema.ContratoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            cliente_id = request.json["cliente_id"]
            consorcio_id = request.json["consorcio_id"]
            valor = request.json["valor"]
            novo_contrato = contrato.Contrato(cliente_id=cliente_id, consorcio_id=consorcio_id, valor=valor)
            resultado = contrato_service.cadastrar_contrato(novo_contrato)
            x = cs.jsonify(resultado)
            return make_response(x, 201)

class ContratoDetail(Resource):
    @jwt_required()
    def get(self, id):
        contrato = contrato_service.listar_contrato_id(id)
        if contrato is None:
            return make_response(jsonify("Contrato não foi encontrado"), 404)
        cs = contrato_schema.ContratoSchema()
        return make_response(cs.jsonify(contrato), 200)

    @jwt_required()
    def put(self, id):
        contrato_bd = contrato_service.listar_contrato_id(id)
        if contrato_bd is None:
            return make_response(jsonify("Contrato não foi encontrado"), 404)
        cs = contrato_schema.ContratoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            cliente_id = request.json["cliente_id"]
            consorcio_id = request.json["consorcio_id"]
            valor = request.json["valor"]
            novo_contrato = contrato.Contrato(cliente_id=cliente_id, consorcio_id=consorcio_id, valor=valor)
            contrato_service.atualiza_contrato(contrato_bd, novo_contrato)
            contrato_atualizado = contrato_service.listar_contrato_id(id)
            return make_response(cs.jsonify(contrato_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        contrato_bd = contrato_service.listar_contrato_id(id)
        if contrato_bd is None:
            return make_response(jsonify("Contrato não encontrado"), 404)
        contrato_service.remove_contrato(contrato_bd)
        return make_response('Contrato excluído com sucesso', 204)

api.add_resource(ContratoList, '/contratos')
api.add_resource(ContratoDetail, '/contratos/<int:id>')
