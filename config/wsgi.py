import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

if os.getenv("DJANGO_AUTO_MIGRATE", "False").lower() in ("1", "true", "yes"):
    try:
        from django.core.management import call_command
        call_command("migrate", interactive=False)
    except Exception:
        pass
