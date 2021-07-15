
import sys, logging, json

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from rest_framework.decorators import action
from rest_framework.response import Response

from hr.people.serializers import PeopleSerializer
from .models import People

from datetime import datetime,date

import pandas as pd
            
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
                Request example: curl -s -X DELETE -H 'Content-type: application/json' "https://colibri.data-ai.com/people/delete-one/?id=1"  <br>
                Supply querystring parameter id|(int)
            </pre>
        """
        try:
            
            person_id = request.query_params["id"]
            
            person = People.objects.get(id=person_id)

            person.delete()
            
            response = {"status":"ok","msg": "Record successfully deleted."}
                        
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
            
            Request example: curl -s -X PATCH -H 'Content-type: application/json' -d '{"id": 98,"salary":1129}' "https://colibri.data-ai.com/people/update-one/" <br>
            
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
                
                response = {"status": "ok","data": serializer.data}
                
            else:
                
                response = {"status":"error","msg":"Failed to update record."}

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
                Request example: curl -s -X GET -H 'Content-type: application/json' "https://colibri.data-ai.com/people/fetch-one/?id=1"  <br>
                Supply querystring parameter id|(int)
            </pre>
        """
        try:
            person_id = request.query_params["id"]
            
            person = People.objects.get(id=person_id)
            
            serializer = self.get_serializer_class()(person)
            
            response = {"status":"error","data":serializer.data}
            
        except Exception as e:
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status": "error","msg": "Please provide an id for your query e.g. /people/fetch-one/?id=<int>"}
            
        return Response(response)
        
    #---overwrite queryset
    
    def get_queryset(self):
        return People.objects
        
#----age 

def age(born):
    
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class StatsViewSet(MongoModelViewSet):
    
    lookup_field = 'id'
    
    queryset = People.objects.all()
    
    logging.basicConfig(filename="access.log",level=logging.INFO)
    logging.basicConfig(filename= "error.log",level=logging.ERROR)
    logger = logging.getLogger('human_api')
    
    serializer_class = PeopleSerializer
    
    mongo_people = People.objects.as_pymongo()

    df = pd.DataFrame(list(mongo_people))
    df = df[df.industry.values != "n/a" ]
    df = df[df.salary.notna()]
    
    df.date_of_birth = df["date_of_birth"].apply(lambda x: datetime.strptime(x,"%d/%m/%Y"))
    
    df["age"] = df.date_of_birth.apply(lambda x:  age(x))
    
    #---averag age by industry
    
    @action(methods=['GET'], detail=False,url_path="avg-age-by-industry")
    def avg_age_industry(self,request):
        """
            <pre>Returns list of average employee ages by industry</pre>
        """
        
        try:
            
            avg_age = self.df.groupby('industry')['age'].mean().T
            
            avg_age = avg_age.to_json()
            
            response = {"status":"ok","data":json.loads(avg_age)}
            
        except Exception as e:
            
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status":"error","msg":"Failed to compute average age by industry."}
            
        return Response(response)
    
    #---average salary by industry
    
    @action(methods=['GET'], detail=False,url_path="avg-salary-by-industry")
    def avg_salary_industry(self,request):
        
        """
            <pre>Returns list of average salaries by industry</pre>
        """
        
        try:
        
            avg_salary = self.df.groupby('industry')['salary'].mean().T
            
            avg_salary = avg_salary.to_json()
            
            response = {"status":"ok","data":json.loads(avg_salary)}
        
        except Exception as e:
            
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status":"error","msg":"Failed to compute average salary by industry."}
            
        return Response(response)
    
    #---average salary by experience
    
    @action(methods=['GET'], detail=False,url_path="avg-salary-per-experience")
    def avg_salary_experience(self,request):
        
        """
            <pre>Returns the average salary per year of experience</pre>
        """
        
        try:
        
            total_salary = self.df.salary.sum()
            total_experience = self.df.years_of_experience.sum()
            
            avg_salary_exp = total_salary/total_experience
            
            avg_salary_exp = "£{:,.2f}".format((avg_salary_exp))
            
            response = {"status":"ok","avg_salary_per_year_of_experience": avg_salary_exp}
        
        except Exception as e:
            
            _,_,c = sys.exc_info()

            self.logger.error("{0} | {1}".format(c.tb_lineno,str(e)))
            
            response = {"status":"error","msg":"Failed to compute average salary per year of experience."}
        
        return Response(response)
    
    #---overwrite queryset
    
    def get_queryset(self):
        return People.objects