from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Organization



class Command(BaseCommand):
    def handle(self, *args, **options):
        organization=[
            {'name':'Рога и копыта','site':'','location':'Черноморск','adress':'unknown','zip_code':'420075'},
            {'name':'Рога и копыта','site':'','location':'Черноморск','adress':'unknown','zip_code':'420075'}
        ]

        for org in organization:
            org_inst=Organization(**org)
            org_inst.full_clean()
            org_inst.save()

