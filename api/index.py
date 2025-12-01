from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

def handler(request, context):
    return app(request, context)
