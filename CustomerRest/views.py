from Customer.models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all().order_by('name')
    serializer_class = PropertySerializer

class PartyViewSet(ModelViewSet):
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all().order_by('name')
    serializer_class = AddressSerializer

