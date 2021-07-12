from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from .models import People

from rest_meets_djongo.serializers import DjongoModelSerializer

class PeopleSerializer(mongoserializers.DocumentSerializer):
    
    class Meta:
        model = People
        fields = '__all__'
        #fields = ["id","first_name","last_name","email","date_of_birth","industry","salary","years_of_experience"]
        