"""
WSGI config for my_first_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settingsEnv = "my_first_project.settings."+ os.environ.get('DJANGO_ENV')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settingsEnv)

application = get_wsgi_application()
