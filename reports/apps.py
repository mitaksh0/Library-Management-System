# from django.apps import AppConfig
# from celery import Celery
# import os

# class ReportsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'reports'

# # Initialize Celery
# app = Celery('reports', broker='amqp://guest@localhost//')
# # app = Celery('reports', broker='pyamqp://guest@localhost//')

# # # Optional: Add configurations
# # app.conf.update(
# #     result_backend='rpc://',
# #     task_serializer='json'
# # )

# # # Import all tasks in the 'reports' module
# app.autodiscover_tasks(['reports'])
# # app.conf.task_routes = {
# #     'reports.tasks.store_report': {'queue': 'report_queue'},
# # }