<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-schedule-commands.svg?maxAge=3600)](https://pypi.org/project/django-schedule-commands/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-schedule-commands.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-schedule-commands.py/actions)

### Installation
```bash
$ [sudo] pip install django-schedule-commands
```

#### Features
+   database/models based
+   `Command` model
    +   `repeat_seconds`
    +   `is_pending` - set to `True` to run
    +   `is_disabled` - set to `True` to disable
    +   `is_logged` - set to `True` to log
+   `Log` model (`command`,`started_at`,`completed_at`)
+   `Exc` model (`command`,`exc_type`,`exc_value`,`exc_traceback`,`created_at`)
+   `scheduler` daemon command

##### `settings.py`
```python
INSTALLED_APPS+=['django_schedule_commands']
```

##### migrate
```bash
$ python manage.py migrate
```

#### Examples
cli
```bash
$ python manage.py scheduler "group1"   # daemon
$ python manage.py scheduler "group2"   # daemon
$ python manage.py run_pending "group1" # run pending commands and exit
```

```python
from django_schedule_commands.models import Command, Group

group = Group.objects.get(name="group1")
group.run_pending()

command = Command.objects.get(name='name')
command.call_command()
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
