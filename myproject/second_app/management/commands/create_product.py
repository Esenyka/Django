from django.core.management.base import BaseCommand
from second_app.models import Product, Client, Order


class Command(BaseCommand):
    help = "Append product"

    def handle(self, *args, **kwargs):
        product = Product(name="Bread", description="fresh, beautiful, wonderful bread", price=12.10, product_quantity=3)
        product.save()
        self.stdout.write(str(product))