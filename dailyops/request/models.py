from django.db import models
from operations.models import Info
# Create your models here.


#model to request for leave

class Leave(Info):
    LEAVE_TYPE=(
        ('F','FULLDAY'),
        ('HL','HALFDAY'),
        ('H','HOURS'),
    )
    leave_type=models.CharField(max_length=10,choices=LEAVE_TYPE)
    reason=models.CharField(max_length=100)
    supervisor_email=models.EmailField()
    team_lead_email=models.EmailField()
    no_of_days=models.IntegerField()

    def __str__(self):
        return print( '{} {} need leave beacuse {}'.format(self.firstName,self.lastName,self.reason))

class Tea(Info):
    OPTION=(
        ('T','TEA'),
        ('C','COFFEE'),
    )
    WITH=(
        ('S','SUGAR'),
        ('N','NOSUGAR'),
    )
    need=models.CharField(max_length=10,choices=OPTION)
    sugar=models.CharField(max_length=10,choices=WITH)

    def __str__(self):
        return print( '{} {} wants {}'.format(self.firstName,self.lastName,self.need))