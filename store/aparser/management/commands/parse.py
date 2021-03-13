from django.core.management.base import BaseCommand
from .parser.parser1 import Parser1


class Command(BaseCommand):
    """control command for parsing"""
    help = "Site parsing"

    def add_arguments(self, parser):
        """add argument for parser what control count of pages for parsing"""
        parser.add_argument('count', type=int, help='Count of pages for parsing')

    def handle(self, *args, **kwargs):
        """control command"""
        count = kwargs['count']

        parser = Parser1()
        parser.start_pars(count)
        parser.stop_pars()
