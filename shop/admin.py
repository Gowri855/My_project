from django.contrib import admin
from .models import *

"""from .models import Category, SubCategory, Product
# Optional: Show subcategories inline within categories
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'trending', 'created_at']
    inlines = [SubCategoryInline]
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status', 'trending', 'created_at']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'vendor', 'quantity', 'selling_price', 'status', 'trending', 'created_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)"""


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)