from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from hr.people.serializers import PersonSerializer
from .models import Person


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-first_name')
    serializer_class = PersonSerializer



