import random

from django.db.transaction import atomic
from faker import Faker

from departments.models import Department, Employee

fake = Faker(locale="ru_RU")


def create_departments():
    departments = []
    for department in range(25):
        parent = random.choice(
            departments
        ) if departments and random.random() > 0.5 else None
        department = Department.objects.create(
            name=fake.company(), parent=parent
        )
        departments.append(department)
    return departments


def create_employees(departments):
    employees = []

    for _ in range(50_000):
        employees.append(
            Employee(
                full_name=fake.name(),
                position=fake.job(),
                date_hired_at=fake.date_this_decade(),
                salary=fake.pydecimal(
                    left_digits=5,
                    right_digits=2,
                    positive=True,
                ),
                department=random.choice(departments),
            )
        )
    Employee.objects.bulk_create(employees, batch_size=1000)


@atomic
def populate():
    departments = create_departments()
    create_employees(departments)
