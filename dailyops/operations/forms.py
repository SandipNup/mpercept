from django.forms import ModelForm
from .models import Operations

class OperationForm(ModelForm):
    class Meta:
        model = Operations
        fields= '__all__'

