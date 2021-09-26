from django.core.management.base import BaseCommand
from users.models import User
from users.models import UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            userprofile = UserProfile.objects.create(user=user)
            userprofile.save()