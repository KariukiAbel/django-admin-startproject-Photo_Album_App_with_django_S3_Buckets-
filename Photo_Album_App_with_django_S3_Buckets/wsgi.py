"""
WSGI config for Photo_Album_App_with_django_S3_Buckets project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Photo_Album_App_with_django_S3_Buckets.settings')

application = get_wsgi_application()
