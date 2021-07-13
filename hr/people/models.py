from mongoengine import Document
from mongoengine.base.fields import ObjectIdField
from mongoengine.fields import FloatField, IntField, StringField

class People(Document):
    _id = ObjectIdField(validation=None)
    id = IntField(unique=True)
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    date_of_birth = StringField()
    industry = StringField()
    salary = FloatField()
    years_of_experience = FloatField()
