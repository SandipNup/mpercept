from django.db import models
from common.choices import DEPARTMENT

# Create your models here.

class Info(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    departments=models.CharField(max_length=10,choices=DEPARTMENT)

    def __str__(self):
        return print( '{} {}'.format(self.firstName,self.lastName))

class Operations(Info):
    OPERATION=(
        ('U','UTENSILS'),
        ('H','HALL'),
    )
    operation=models.CharField(max_length=1,choices=OPERATION)
    
    def __str__(self):
        return print( '{} {} has to perform {}'.format(self.firstName,self.lastName,self.operation))
