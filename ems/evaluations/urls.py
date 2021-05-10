from django.urls import path
from .views import EvaluationCreationView, EvaluationDetailView, EvaluationListView, EvaluationDeleteView

app_name = "evaluations"

urlpatterns = [
    path('', EvaluationListView.as_view(),
         name="evaluations-view"),
    path('<int:pk>/evaluate', EvaluationCreationView.as_view(),
         name="evaluation-create"),
    path('me', EvaluationDetailView.as_view(),
         name="evaluation-detail"),
    path('me', EvaluationDetailView.as_view(),
         name="evaluation-detail"),

    path('<int:pk>/delete', EvaluationDeleteView.as_view(),
         name="evaluation-delete"),
]
