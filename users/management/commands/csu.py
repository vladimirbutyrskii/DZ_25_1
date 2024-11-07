from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin1@example.com",
            first_name="Admin",
            last_name="SkyPro",
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("123qwe")
        user.save()
