import os
import django
from django.core.files.storage import default_storage
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'g_project.settings')
django.setup()

from shop.models import Product

def migrate_product_images():
    products = Product.objects.all()
    count = 0
    
    for product in products:
        if product.productimage and not product.productimage.name.startswith('http'):
            try:
                # This will upload to Cloudinary
                print(f"Migrating: {product.name}")
                product.save()
                count += 1
            except Exception as e:
                print(f"Error migrating {product.name}: {e}")
    
    print(f"\nMigrated {count} products successfully!")

if __name__ == "__main__":
    migrate_product_images()
