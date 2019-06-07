from django.forms import ModelForm
from .models import Leave,Tea


class LeaveForm(ModelForm):
    class Meta:
        model=Leave
        fields='__all__'

class TeaForm(ModelForm):
    class Meta:
        model=Tea
        fields='__all__'