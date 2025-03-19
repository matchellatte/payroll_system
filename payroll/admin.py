from django.contrib import admin
from .models import Employee, Wage, Payroll

admin.site.register(Employee)
admin.site.register(Wage)
admin.site.register(Payroll)
