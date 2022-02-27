import os
from django.core.asgi import get_asgi_application
# enable Django to use our configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
