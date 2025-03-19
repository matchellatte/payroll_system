from django.db import models
from decimal import Decimal

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Wage(models.Model):
    wage_id = models.AutoField(primary_key=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_wage(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.hourly_rate:.2f}-{self.hours_worked:.2f}"

    

class Payroll(models.Model):
    PAYMENT_CHOICES = [("Full Payment", "Full Payment"), ("Installment", "Installment")]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Prevent duplicate payrolls
    wage = models.OneToOneField(Wage, on_delete=models.CASCADE)
    date_generated = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    @property
    def tax(self):
        tax_rate = Decimal("0.15")  # Convert float to Decimal
        return self.wage.total_wage * tax_rate if self.wage.total_wage > Decimal("30000") else Decimal("0")

    @property
    def final_wage(self):
        return self.wage.total_wage - self.tax

    
    
