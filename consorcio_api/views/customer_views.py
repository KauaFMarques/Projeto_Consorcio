from flask_restful import Resource
from consorcio_api import api
from ..schemes import customer_schemes
from flask import request, make_response, jsonify
from ..entidades import customer
from ..service import customer_service
from ..views import paginate
from ..models.customer_model import Customer
from flask_jwt_extended import jwt_required

class ClienteList(Resource):
    @jwt_required()
    def get(self):
        cs = customer_schemes.ClienteSchema(many=True)
        return paginate(Customer, cs)

    @jwt_required()
    def post(self):
        cs = customer_schemes.CustomerSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            endereco = request.json["endereco"]
            telefone = request.json["telefone"]
            novo_cliente = customer.Customer(nome=nome, endereco=endereco, telefone=telefone)
            resultado = customer_service.cadastrar_cliente(novo_cliente)
            x = cs.jsonify(resultado)
            return make_response(x, 201)

class ClienteDetail(Resource):
    @jwt_required()
    def get(self, id):
        cliente = customer_service.listar_cliente_id(id)
        if cliente is None:
            return make_response(jsonify("Cliente não foi encontrado"), 404)
        cs = customer_schemes.CustomerSchema()
        return make_response(cs.jsonify(cliente), 200)

    @jwt_required()
    def put(self, id):
        cliente_bd = customer_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não foi encontrado"), 404)
        cs = customer_schemes.CustomerSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            endereco = request.json["endereco"]
            telefone = request.json["telefone"]
            novo_cliente = customer.Customer(nome=nome, endereco=endereco, telefone=telefone)
            customer_service.atualiza_cliente(cliente_bd, novo_cliente)
            cliente_atualizado = customer_service.listar_cliente_id(id)
            return make_response(cs.jsonify(cliente_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        cliente_bd = customer_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não encontrado"), 404)
        customer_service.remover_cliente(cliente_bd)
        return make_response('Cliente excluído com sucesso', 204)

api.add_resource(ClienteList, '/clientes')
api.add_resource(ClienteDetail, '/clientes/<int:id>')
