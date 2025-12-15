from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Load product data if database is empty'

    def handle(self, *args, **options):
        from shop.models import Product
        
        # Check if products already exist
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING('Products already exist. Skipping data load.'))
            return
        
        # Load the data
        fixture_path = 'products_data.json'
        if os.path.exists(fixture_path):
            self.stdout.write('Loading product data...')
            call_command('loaddata', fixture_path)
            self.stdout.write(self.style.SUCCESS('✓ Product data loaded successfully!'))
        else:
            self.stdout.write(self.style.ERROR(f'Fixture file not found: {fixture_path}'))
