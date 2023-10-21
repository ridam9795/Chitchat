"""
ASGI config for wbbackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import sketchboard.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wbbackend.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(sketchboard.routing.websocket_pattern)
        
})


