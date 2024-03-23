# oil_selector_app/admin.py

from django.contrib import admin
from .models.car import Car, CarMake, CarModel, CarEngine
from .models.product import Category, Product, ProductVariant, RecommendedProduct

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'is_active', 'created_at', 'updated_at')

class CarEngineAdmin(admin.ModelAdmin):
    list_display = ('engine_type', 'is_active', 'created_at', 'updated_at')

class CarAdmin(admin.ModelAdmin):
    list_display = ('year', 'model', 'engine', 'is_active', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'sku', 'unit')
    search_fields = ('product', 'sku')

class RecommendedProductAdmin(admin.ModelAdmin):
    list_display = ('car_display', 'product', 'is_active', 'created_at', 'updated_at')

    def car_display(self, obj):
        return f"{obj.car.year} {obj.car.model.make} {obj.car.model} - {obj.car.engine.engine_type}"


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarEngine, CarEngineAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(RecommendedProduct, RecommendedProductAdmin)
