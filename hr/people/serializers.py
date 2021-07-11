from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name','last_name', 'email', 'date_of_birth', 'industry', 'salary','years_of_experience']


