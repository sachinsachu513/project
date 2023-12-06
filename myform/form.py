from django import forms
from.models import employees


class employeeform(forms.ModelForm):
    class Meta:
        model=employees
        fields="__all__"