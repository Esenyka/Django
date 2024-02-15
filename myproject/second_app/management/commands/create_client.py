from django.core.management.base import BaseCommand
from second_app.models import Client


class Command(BaseCommand):
    help = "Create client"

    def handle(self, *args, **kwargs):
        client = Client(name="Petr", email="pert@mail.com", phone_number=89527652212, address="Pushkina 48")
        client.save()
        self.stdout.write(str(client))