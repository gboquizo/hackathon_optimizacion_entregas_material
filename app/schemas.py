"""

Map a database model to json data
Schemas are equivalent to Django serializers.

"""
from app import ma
from .models import *


class DonorSchema(ma.Schema):

    class Meta:
        model = Donor
        sqla_session = db.session
        fields = ('user', 'address', 'updated_at')

class AddressSchema(ma.Schema):

    class Meta:
        model = Donor
        sqla_session = db.session
        fields = ('state', 'city', 'postal_code', 'street', 'number', 'extra_details_address')