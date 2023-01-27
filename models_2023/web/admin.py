from django.contrib import admin

from models_2023.web.models import Employee, Department, Project, AccessCard


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level')
    list_filter = ('level',)
    search_fields = ('first_name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessCard)
class AccessCardAdmin(admin.ModelAdmin):
    pass
