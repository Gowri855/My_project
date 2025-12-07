from django.contrib import admin
from .models import Category, SubCategory, Product

# Optional: Show subcategories inline within categories
class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'trending', 'created_at']
    inlines = [SubCategoryInline]

class SubCategoryAdmin(admin.ModelAdmin):
    # ✅ FIXED: Removed 'status', 'trending', 'created_at' - SubCategory doesn't have these
    list_display = ['id', 'name', 'category']  
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'vendor', 'quantity', 'selling_price', 'status', 'trending', 'created_at']
    search_fields = ('name', 'description')
    list_filter = ('subcategory__category', 'subcategory', 'status', 'trending')

# Register models with their admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
