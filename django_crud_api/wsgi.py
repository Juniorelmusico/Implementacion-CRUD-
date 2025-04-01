"""
WSGI config for django_crud_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
>>>>>>> origin/master
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_crud_api.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_crud_api.settings')
>>>>>>> origin/master

application = get_wsgi_application()
