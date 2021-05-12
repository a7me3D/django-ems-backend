from django.urls import path
from .views import *
app_name = "conges"

urlpatterns = [
    path('', CongeListView.as_view(), name="conge-view"),
    path('me', CongeEmployeeListView.as_view(), name="conge-employee"),
    path('create', CongeCreationView.as_view(), name="conge-create"),
    path('<int:pk>', CongeDetailView.as_view(), name="conge-detail"),
    path('<int:pk>/update/', CongeUpdateView.as_view(),
         name='conge-update'),
    path('<int:pk>/delete/', CongeDeleteView.as_view(),
         name='conge-delete'),
    path('<int:pk>/accept/', CongeAcceptView.as_view(),
         name='conge-accept'),
    path('<int:pk>/reject', CongeRejectView.as_view(),
         name='conge-reject')
]
