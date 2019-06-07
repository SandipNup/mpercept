from django.db import models
from operations.models import Info

# Create your models here.

class Booking(Info):
    ROOM=(
        (1,'T0'),
        (2,'A0'),
        (3,'A1'),
    )
    meeting_room=models.CharField(max_length=10,choices=ROOM)

    def __str__(self):
        return print( '{} {} wants to book {}'.format(self.firstName,self.lastName,self.meeting_room))