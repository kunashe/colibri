
import sys, logging

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from rest_framework.decorators import action
from rest_framework.response import Response

from hr.people.serializers import PeopleSerializer
from .models import People

class PeopleViewSet(MongoModelViewSet):

    lookup_field = 'id'
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
    logging.basicConfig(filename="access.log",level=logging.INFO)
    logging.basicConfig(filename= "error.log",level=logging.ERROR)
    logger = logging.getLogger('human_api')
    
    #---delete person
    
    @action(methods = ['DELETE'], detail=False,url_path="delete-one")
    def delete_one(self,request):
        """
            <pre>
                Deletes single instance of Person <br>
                Request example: curl -s -X DELETE -H 'Content-type: application/json' "http://127.0.0.1:8000/people/delete-one/?id=1"  <br>
                Supply querystring parameter id|(int)
            </pre>
        """
        try:
            
            person_id = request.query_params["id"]
            
            person = People.objects.get(id=person_id)

            person.delete()
            
            response = {"status":"ok","msg": "Record successfully deleted."}
            
            return Response(response)
            
        except Exception as e:
            
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status":"error","msg":"Failed to delete record."}
            
            return Response(response)
            
    #---update person
    
    @action(methods = ['POST','PUT','PATCH'], detail=False,url_path="update-one")
    def update_one(self,request):
        """<pre>
            Updates single instance of Person <br>
            
            Request example: curl -s -X PATCH -H 'Content-type: application/json' -d '{"id": 98,"salary":1129}' "http://127.0.0.1:8000/people/update-one/" <br>
            
            Supply JSON object:
                - Required fields: "id|(int)" field
                - Optional fields:  ['first_name','last_name', 'email', 'date_of_birth', 'industry', 'salary|(float)','years_of_experience|(float)']
            </pre>
        """
        try:

            person_id = request.data["id"]
            person = People.objects.get(id=person_id)
            serializer = self.get_serializer_class()(person,data=request.data)

            if serializer.is_valid():

                params = {}
                params = request.data
                
                person = People.objects(id=person_id)
                person.update(**params)
                
                serializer = self.get_serializer_class()(People.objects.get(id=person_id))
                
                return Response(serializer.data)
            else:
                
                response = {"status":"error","msg":"Failed to update record."}
                return Response(response)

        except Exception as e:
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status":"error","msg":"Failed to update record."}
            return Response(response)
    
    #---fetch person
    
    @action(methods=['GET'], detail=False,url_path="fetch-one")
    def fetch_one(self,request):
        """
            <pre>
                Retrieves single instance of Person <br>
                Request example: curl -s -X GET -H 'Content-type: application/json' "http://127.0.0.1:8000/people/fetch-one/?id=1"  <br>
                Supply querystring parameter id|(int)
            </pre>
        """
        try:
            person_id = request.query_params["id"]
            
            person = People.objects.get(id=person_id)
            
            serializer = self.get_serializer_class()(person)
            
            return Response(serializer.data)
            
        except Exception as e:
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status": "error","msg": "Please provide an id for your query e.g. /people/fetch-one/?id=<int>"}
            
            return Response(response)
    
    #---overwrite queryset
    
    def get_queryset(self):
        return People.objects
        
