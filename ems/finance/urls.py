from django.urls import path
from .views import *
app_name = "finances"

urlpatterns = [
    path('', FinanceListView.as_view(), name="finance-view"),
    path('me', FinanceEmployeeListView.as_view(), name="finance-employee"),
    path('create', FinanceCreationView.as_view(), name="finance-create"),
    path('<int:pk>', FinanceDetailView.as_view(), name="finance-detail"),
    path('<int:pk>/update/', FinanceUpdateView.as_view(),
         name='finance-update'),
    path('<int:pk>/delete/', FinanceDeleteView.as_view(),
         name='finance-delete'),
    path('<int:pk>/accept/', FinanceAcceptView.as_view(),
         name='finance-accept'),
    path('<int:pk>/reject', FinanceRejectView.as_view(),
         name='finance-reject')
]
