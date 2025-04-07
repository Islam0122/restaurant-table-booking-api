from .base import *

DEBUG = False

# Тестовая БД (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Отключаем кэширование
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
TEST_RUNNER = 'pytest_django.runner.DiscoverRunner'
