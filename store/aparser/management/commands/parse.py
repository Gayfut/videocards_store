from django.core.management.base import BaseCommand
from .parser.parser1 import Parser1


class Command(BaseCommand):
    help = "Парсинг сайта"

    def handle(self, *args, **options):
        parser = Parser1()
        parser.start_pars(1)
        parser.stop_pars()
