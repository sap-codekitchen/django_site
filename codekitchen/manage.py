#!/usr/bin/env python
import os
import sys

extra_folders = [
    '/afs/athena.mit.edu/dept/cron/project/codekitchen/web_scripts/django',
]
for folder in extra_folders:
    sys.path.append(folder)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codekitchen.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
