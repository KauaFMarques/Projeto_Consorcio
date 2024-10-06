from api import ma
from models.consortium_model import Consortium

class ConsortiumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Consortium
        load_instance = True
