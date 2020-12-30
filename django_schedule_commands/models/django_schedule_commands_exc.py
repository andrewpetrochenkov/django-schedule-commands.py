from django.db import models


class Exc(models.Model):
    command = models.ForeignKey(
        'Command', related_name="exc_set", on_delete=models.CASCADE)
    exc_type = models.TextField()
    exc_value = models.TextField()
    exc_traceback = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'django_schedule_commands_exc'
        indexes = [
            models.Index(fields=["command"],),
            models.Index(fields=["-created_at"],),
        ]
