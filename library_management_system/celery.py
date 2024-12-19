from celery import Celery
from django.conf import settings
import os
# import reports

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management_system.settings')

# Initialize Celery
# app = Celery('library_management_system', broker='amqp://guest@localhost//')
app = Celery('library_management_system', broker='redis://red-cti553t6l47c738fehng:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in all Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)