from rest_framework import serializers
from .models import *


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
    




