from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from .models import People

class PeopleSerializer(mongoserializers.DocumentSerializer):
    
    class Meta:
        model = People
        fields = '__all__'
        