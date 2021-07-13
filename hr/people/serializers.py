from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import People

class PeopleSerializer(DocumentSerializer):
    
    class Meta:
        model = People
        fields = '__all__'
        