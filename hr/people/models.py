from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    years_of_experience = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
