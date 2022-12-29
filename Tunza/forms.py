from django import forms
from Tunza.models import Msgs



class Table(forms.ModelForm):
    class Meta:
        model = Msgs
        fields = '__all__'

