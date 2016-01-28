"""
WSGI config for foundation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys 

sys.path = ["/home/webdev/Dokumen/foundation"] + sys.path
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foundation.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "foundation.settings"
#import django.core.handlers.wsgi
application = get_wsgi_application()
#application = django.core.handlers.wsgi.WSGIHandler()
