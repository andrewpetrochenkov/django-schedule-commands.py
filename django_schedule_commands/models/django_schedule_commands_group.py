import gc
from datetime import datetime
from django.db import models

from .django_schedule_commands_command import Command


class Group(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'django_schedule_commands_group'
        indexes = [
            models.Index(fields=["name"],),
        ]

    def run_pending(self):
        command_list = list(Command.objects.filter(
            group=self).exclude(is_disabled=True).order_by('completed_at').all())
        for command in command_list:
            if command.is_pending or not command.completed_at or datetime.now() >= command.expired_at:
                command.call_command()
        gc.collect()
