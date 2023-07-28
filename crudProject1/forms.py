from django import forms
from crudProject1.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['firstname', 'lastname', 'email']
