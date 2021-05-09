from django.urls import path
from .views import EvaluationCreationView

app_name = "evaluations"

urlpatterns = [
    path('create', EvaluationCreationView.as_view(), name="evaluation-create"),
]
