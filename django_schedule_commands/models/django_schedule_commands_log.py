from django.db import models


class Log(models.Model):
    command = models.ForeignKey(
        'Command', related_name="log_set", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField()

    class Meta:
        db_table = 'django_schedule_commands_log'
        indexes = [
            models.Index(fields=["command"],),
            models.Index(fields=["-completed_at"],),
        ]
