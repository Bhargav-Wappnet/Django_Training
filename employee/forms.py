from django import forms
from employee.models import employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"
