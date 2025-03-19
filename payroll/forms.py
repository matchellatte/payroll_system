from django import forms
from .models import Payroll

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ["employee", "wage"]

    def clean_employee(self):
        employee = self.cleaned_data.get("employee")
        if Payroll.objects.filter(employee=employee).exists():
            raise forms.ValidationError("Payroll entry already exists for this employee.")
        return employee
