from django.contrib import admin

from departments.models import Department, Employee


# Register your models here.


class EmployeeInline(admin.TabularInline):
    model = Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass