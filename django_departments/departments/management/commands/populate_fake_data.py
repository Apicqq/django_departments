from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from core.data_factories import populate_employees_and_departments

        populate_employees_and_departments()
