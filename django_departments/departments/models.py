from django.db import models


class Department(models.Model):
    name = models.CharField("Название департамента", max_length=100)
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
    # TODO Добавить констрейнты на имя (не пустое), должность (не пустое),
    #  зарплата (больше 0), дата приема (не будущая), не пустое подразделение,
    #  не более одного подразделения у сотрудника
    full_name = models.CharField("ФИО", max_length=100)
    position = models.CharField("Должность", max_length=100)
    date_hired_at = models.DateField("Дата приема на работу")
    salary = models.DecimalField("Зарплата", max_digits=10, decimal_places=2)
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
        constraints = [
            # ...
            #TODO add later!
        ]

    def __str__(self):
        return f"{self.pk}: {self.full_name} - {self.position}"
