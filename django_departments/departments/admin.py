from django.contrib import admin

from departments.models import Department, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 0
    readonly_fields = ("full_name", "position", "date_hired_at", "salary")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "employee_count")
    inlines = [EmployeeInline]

    @admin.display(description="Количество сотрудников в подразделении")
    def employee_count(self, obj):
        return obj.employees.count()


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
