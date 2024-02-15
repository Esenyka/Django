from django.core.management.base import BaseCommand
from second_app.models import Product, Client, Order


class Command(BaseCommand):
    help = "Append product"

    def add_arguments(self, parser):
        parser.add_argument('pk_c', type=int, help='Client ID')
        parser.add_argument('pk_p', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk_c = kwargs.get('pk_c')
        pk_p = kwargs.get('pk_p')
        client = Client.objects.filter(pk=pk_c).first()
        produc = Product.objects.filter(pk=pk_p).first()
        total_am = produc.price * produc.product_quantity
        order = Order(customer=client, total_amount=total_am)
        order.save()