from django.urls import path

from departments.views import DepartmentListView

app_name = "departments"

urlpatterns = [
    path("list/", DepartmentListView.as_view(), name="list"),
]