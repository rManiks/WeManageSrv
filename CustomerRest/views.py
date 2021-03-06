from Customer.models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import ArtifactSerializer, PropertySerializer, AddressSerializer, InspectionEventSerializer, PartySerializer

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all().order_by('name')
    serializer_class = PropertySerializer

class PartyViewSet(ModelViewSet):
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all().order_by('name')
    serializer_class = AddressSerializer

class InspectionViewSet(ModelViewSet):
    queryset = InspectionEvent.objects.all()
    serializer_class = InspectionEventSerializer

class ArtifactViewSet(ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer