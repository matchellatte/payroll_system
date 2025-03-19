from django.shortcuts import render, redirect
from .models import Payroll
from .forms import PayrollForm
from django.contrib import messages

def payroll_form(request):
    if request.method == "POST":
        payroll_form = PayrollForm(request.POST)

        if payroll_form.is_valid():
            payroll_form.save()
            messages.success(request, "Payroll entry added successfully!")
            return redirect("index")
    else:
        payroll_form = PayrollForm()

    return render(request, "payroll/payroll_form.html", {"payroll_form": payroll_form})

def index(request):
    payrolls = Payroll.objects.all()

    # Compute grand totals for each column
    grand_total_wage = sum(p.wage.total_wage for p in payrolls)
    grand_total_tax = sum(p.tax for p in payrolls)
    grand_final_wage = sum(p.final_wage for p in payrolls)

    context = {
        "payrolls": payrolls,
        "grand_total_wage": grand_total_wage,
        "grand_total_tax": grand_total_tax,
        "grand_final_wage": grand_final_wage,
    }

    return render(request, "payroll/index.html", context)

