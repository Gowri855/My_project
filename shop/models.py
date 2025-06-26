from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime
import os

def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = "%s_%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False, help_text="0-show, 1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} > {self.name}"

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, null=True)
    vendor = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    quantity = models.IntegerField()
    original_price = models.FloatField()
    selling_price = models.FloatField()
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False, help_text="0-show, 1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.subcategory.name} > {self.name}"
