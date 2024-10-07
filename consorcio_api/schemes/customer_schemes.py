# customer_schemes.py
from consorcio_api import ma

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = 'consorcio_api.models.customer_model.Customer'  # Use a string reference
        load_instance = True
