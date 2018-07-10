from .base import *
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.amazonaws.com',
]

# STATIC
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
# 뒤에 오는 모든 파일은 동적이 아닌 static으로 처리한다.
STATIC_URL = '/static/'

# WSGI
WSGI_APPLICATION = 'config.wsgi.local.application'

# DB

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
