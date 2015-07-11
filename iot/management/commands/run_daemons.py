# probably need another command later, keep as reference
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        from iot.daemon_runner import *
        runAll()