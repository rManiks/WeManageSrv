from rest_framework import serializers
from Customer.models import Party, Address, InspectionEvent, Artifact

class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'address_id', 'avatar')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'line_1', 'line_2', 'city', 'state', 'post_code')

class PropertySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = AddressSerializer(required=False)
    owner = PartySerializer(required=False)
    
class InspectionEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InspectionEvent
        fields = ('effective_date', 'description', 'tax_paid', 'eb_paid', 'maintenance_paid', 'well_maintained', 'tenent_complaints')

class ArtifactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artifact
        fields = ('event_id', 'artefact')


