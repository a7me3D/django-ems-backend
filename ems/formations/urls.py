from django.urls import path
from .views import FormationCreationView, FormationListView, FormationUpdateView, FormationDeleteView, FormationDetailView

app_name = "formations"

urlpatterns = [
    path('', FormationListView.as_view(), name="formation-view"),
    path('create', FormationCreationView.as_view(), name="formation-create"),
    path('<int:pk>/update/', FormationUpdateView.as_view(), name='formation-update'),
    path('<int:pk>/', FormationDetailView.as_view(), name='formation-detail'),
    path('<int:pk>/delete/', FormationDeleteView.as_view(), name='formation-delete'),

]
