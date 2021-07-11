
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from rest_framework.decorators import api_view
from rest_framework.response import Response

from hr.people.serializers import PeopleSerializer
from .models import People

class PeopleViewSet(MongoModelViewSet):

    lookup_field = 'id'
    serializer_class = PeopleSerializer

    def get_queryset(self):
        
        return People.objects.all()

#---update person 

@api_view(['GET'])
def update_person(request,id):

    person = People.objects(id=id)
    
    serilaizer = PeopleSerializer(instance=person,data=request.data)

    if serilaizer.is_valid():
        print(request)
    return Response(serilaizer.data)


