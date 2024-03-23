# oil_selector_app/management/commands/import_data.py

import csv
import os
import glob
from django.core.management.base import BaseCommand
from oil_selector_app.models import Car, CarModel, CarMake, CarEngine, Category, Product, ProductVariant, RecommendedProduct

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, 'data')
        print(data_dir)
        file_pattern = os.path.join(data_dir, '*.csv')
        file_paths = glob.glob(file_pattern)
        print(file_paths)

        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    car = self.create_car(row)
                    category  = self.create_category(row)
                    product = product = self.create_product(row, category)
                    self.create_product_variant(row, product)
                    self.create_recommended_product(row, car, product)

    def create_car(self, row):
        year = row['Year']
        make_name = row['Make']
        model_name = row['Model']
        engine_type = row['Engine']

        car_make, _ = CarMake.objects.get_or_create(name=make_name)
        car_model, _ = CarModel.objects.get_or_create(name=model_name, make=car_make)
        car_engine, _ = CarEngine.objects.get_or_create(engine_type=engine_type)

        car, _ = Car.objects.get_or_create(year=year, model=car_model, engine=car_engine)
        return car

    def create_category(self, row):
        category_name = row['Category']
        category, _ = Category.objects.get_or_create(name=category_name)
        return category

    def create_product(self, row, category):
        product_name = row['MOTOSEL Item Description']

        product, _ = Product.objects.get_or_create(name=product_name, category=category)
        return product

    def create_product_variant(self, row, product):
        sku = row['MOTOSEL PART NO']
        unit = row['MOTOSEL Package Type']

        product_variant, _ = ProductVariant.objects.get_or_create(product=product, sku=sku, unit=unit)
        return product_variant

    def create_recommended_product(self, row, car, product):
        capacity = row.get('Capacity', '')
        capacity_note = row.get('Capacity Note 1', '')
        recommendation_note = row.get('OEM Recommendation Note 1', '')
        
        recommended_product, created = RecommendedProduct.objects.get_or_create(car=car, product=product)

        recommended_product.capacity = capacity
        recommended_product.capacity_note = capacity_note
        recommended_product.recommendation_note = recommendation_note
        recommended_product.save()