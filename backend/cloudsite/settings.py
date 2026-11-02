"""Test-only settings; deliberately refuse non-local database connections."""
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
INSTALLED_APPS = ["tasks"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True

host = os.environ["POSTGRES_HOST"]
name = os.environ["POSTGRES_DB"]
if host not in {"127.0.0.1", "localhost", "::1"} or name != "cloud_integration":
    raise ValueError("Only a local disposable cloud_integration database is allowed")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": name,
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": host,
        "PORT": os.environ["POSTGRES_PORT"],
        "TEST": {"NAME": "test_cloud_integration"},
    }
}
