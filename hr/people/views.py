
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from hr.people.serializers import PersonSerializer
from .models import People


class PersonViewSet(MongoModelViewSet):

    lookup_field = 'id'
    serializer_class = PersonSerializer

    def get_queryset(self):
        
        return People.objects.all()



