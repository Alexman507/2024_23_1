from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания модератора"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator',
            is_active=True,
            is_staff=True,
        )

        user.set_password('123')
        user.save()
