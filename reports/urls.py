from rest_framework.urls import path
from .views import manage_reports, list_all_reports

urlpatterns = [
    path('report/', manage_reports),
    path('report/all', list_all_reports),
]