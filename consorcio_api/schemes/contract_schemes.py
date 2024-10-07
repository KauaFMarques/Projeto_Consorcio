from consorcio_api import ma
from models.contract_model import Contract
from marshmallow import fields

class ContractSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contract
        load_instance = True

    customer = fields.Nested('CustomerSchema', only=["nome", "idade", "renda_mensal"])
    consortium = fields.Nested('ConsortiumSchema', only=["valor_carro", "parcelas_mensais", "prazo_meses"])