from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender="departments.Department")
def validate_department_hierarchy(sender, instance, **kwargs):
    if not instance.parent:
        return

    level = 0
    parent = instance.parent
    while parent:
        level += 1
        parent = parent.parent
    if level > 5:
        raise ValidationError(
            "Максимальное вложенность подразделений - 5 уровней.",
        )