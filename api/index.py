import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djngoproject1.settings")

app = get_wsgi_application()

def handler(request, context):
    return app(request, context)
