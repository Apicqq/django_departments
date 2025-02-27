from django.db import models

from departments.validators import min_length_validator, validate_hided_at, \
    salary_min_value_validator


class Department(models.Model):
    name = models.CharField(
        "Название департамента",
        max_length=100,
        validators=[
            min_length_validator
        ]
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subdepartments",
        verbose_name="Родительский департамент",
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        return self.name[:30]


class Employee(models.Model):
    full_name = models.CharField(
        "ФИО", max_length=100,
        validators=[min_length_validator]
    )
    position = models.CharField(
        "Должность",
        max_length=100,
        validators=[
            min_length_validator
        ]
    )
    date_hired_at = models.DateField(
        "Дата приема на работу",
        validators=[validate_hided_at]
    )
    salary = models.DecimalField(
        "Зарплата",
        max_digits=10,
        decimal_places=2,
        validators=[salary_min_value_validator]
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Департамент",
        related_name="employees",
    )

    class Meta:
        ordering = ("full_name",)
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.pk}: {self.full_name} - {self.position}"
