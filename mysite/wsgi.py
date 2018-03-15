"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 웹서버가 어떤 요청을 받아 들일것인지 ,

# mysite.settings 파일의 설정 값을 기반으로 웹어플리케이션을 구동하라 는 의미.

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
