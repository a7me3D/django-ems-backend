from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employee-view"),
    path('create', EmployeeCreationView.as_view(), name="employee-create"),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('me/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('me/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('<int:pk>/activate/', EmployeeActivateView.as_view(),
         name='employee-activate'),
    path('<int:pk>/desactivate', EmployeeDesactivateView.as_view(),
         name='employee-desactivate')

]
