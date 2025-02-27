from django.views.generic.list import ListView

from departments.models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = "departments/department_list.html"
    paginate_by = 15
    context_object_name = "departments"
    queryset = Department.objects.filter(parent__isnull=True).prefetch_related(
        "subdepartments", "employees"
    )
