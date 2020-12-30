from django.core.management.base import BaseCommand

from django_schedule_commands.models import Group


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('group', type=str, nargs='?', default=None)

    def handle(self, *args, **options):
        group = Group.objects.get(name=options['group'])
        group.run_pending()
