from django.core.management.base import BaseCommand
from second_app.models import Product


class Command(BaseCommand):
    help = "Update product"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.save()
        self.stdout.write("product was updated " + str(product))

