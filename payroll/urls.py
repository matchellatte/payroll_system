from django.urls import path
from .views import index, payroll_form

urlpatterns = [
    path("", index, name="index"),
    path("add/", payroll_form, name="payroll_form"),
]
