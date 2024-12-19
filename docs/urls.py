from django.urls import path
from . import views

urlpatterns = [
    path('doc/', views.schema_view.with_ui(), name="swagger-ui")
]