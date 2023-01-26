from django.contrib import admin

from models_2023.web.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass