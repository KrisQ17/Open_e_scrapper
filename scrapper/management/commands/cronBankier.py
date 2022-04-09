from django.core.management.base import BaseCommand, CommandError
from scrapper.scripts.BankierScrapper import BankierScrapper

class Command(BaseCommand):

    help = "Cron to scrap Bankier website and save selected data to SQLite database."
    
    def handle(self, *args, **kwargs):
        try:
            scrapper = BankierScrapper()
            scrapper.run()
        except Exception as e:
            raise CommandError(e)