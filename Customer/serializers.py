from .models import *
from rest_framework import serializers


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('name', 'address_id')

class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'address_id', 'avatar')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('name', 'line_1', 'line_2', 'city', 'state', 'post_code')
