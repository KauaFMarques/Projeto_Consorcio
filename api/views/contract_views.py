from flask_restful import Resource
from api import api
from schemas.contract_schema import ContractSchema
from flask import request, make_response, jsonify
from services import contract_service

class ContractList(Resource):
    def get(self):
        contracts = contract_service.listar_contratos()
        cs = ContractSchema(many=True)
        return make_response(cs.jsonify(contracts), 200)

    def post(self):
        cs = ContractSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            customer = request.json["customer"]
            consortium = request.json["consortium"]
            aprovado = request.json["aprovado"]
            novo_contrato = contract_service.cadastrar_contrato(customer, consortium, aprovado)
            return make_response(cs.jsonify(novo_contrato), 201)

api.add_resource(ContractList, '/contracts')
