from django.core.management.base import BaseCommand
from backend.models import Pokemon  # Asegúrate de importar todos los modelos que necesitas

class Command(BaseCommand):
    help = 'Clear all data from the database'

    def handle(self, *args, **kwargs):
        Pokemon.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the database'))