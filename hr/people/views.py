
import sys
import bson.objectid
from mongoengine import queryset
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from hr.people.serializers import PeopleSerializer
from .models import People

class PeopleViewSet(MongoModelViewSet):

    lookup_field = 'id'
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @action(methods = ['POST','PUT','PATCH'], detail=False,url_path="update-one")
    def update_one(self,request):
        
        try:

            person_id = request.data["id"]
            person = People.objects(id=person_id)
            serializer = self.get_serializer_class()(person,data=request.data)

            if serializer.is_valid():

                params = {}
                params = request.data
                
                person = People.objects(id=person_id).update(**params)
                
                return Response(serializer.data)
            else:
                
                return Response('{"status":"Error updating individual\'s data"}')

        except Exception as e:
            _,_,c = sys.exc_info()

            print("{0} | {1}".format(c.tb_lineno,str(e)))
        
    @action(methods=['GET'], detail=False,url_path="fetch-one")
    def fetch_one(self,request):
        
        person_id = request.query_params["id"]
        
        print(person_id)
        person = People.objects(id=32)
        
        serializer = self.get_serializer_class()(person)

        return Response(person.to_json())
        
    def get_queryset(self):
        return People.objects




