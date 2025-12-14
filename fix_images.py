import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from shop.models import Product

# Your image folder
IMAGE_FOLDER = r'E:\MyWhoops\media\uploads'

# Get all products (sorted by ID)
products = Product.objects.all().order_by('id')
print(f"Total products: {products.count()}")

# Get all image files (sorted alphabetically)
image_files = sorted([f for f in os.listdir(IMAGE_FOLDER) 
                     if f.endswith(('.jpg', '.jpeg', '.png', '.webp', '.jfif'))])
print(f"Total images: {len(image_files)}")

# Match first 50 images to first 50 products
for i, product in enumerate(products[:50]):
    if i < len(image_files):
        image_filename = image_files[i]
        product.productimage = f'uploads/{image_filename}'
        product.save()
        print(f"✓ {product.id}: {product.name[:40]}... -> {image_filename}")

print("\n✅ Done! All products now have images!")
