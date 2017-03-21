from .models import *
from rest_framework import viewsets
from .serializers import *

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('name')
    serializer_class = PropertySerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('name')
    serializer_class = AddressSerializer

