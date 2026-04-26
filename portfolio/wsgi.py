"""
WSGI config for portfolio project.

Wraps Django's WSGI app with WhiteNoise so that `/media/` is served from
MEDIA_ROOT in production (the staticfiles middleware only handles /static/).
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
application = WhiteNoise(
    application,
    root=str(settings.MEDIA_ROOT),
    prefix=settings.MEDIA_URL,
)
