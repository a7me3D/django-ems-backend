from django.urls import path
from .views import RecruitmentCreationView, RecruitmentListView, RecruitmentUpdateView, RecruitmentDeleteView, RecruitmentDetailView

app_name = "recruitments"

urlpatterns = [
    path('', RecruitmentListView.as_view(), name="recruitment-view"),
    path('create', RecruitmentCreationView.as_view(), name="recruitment-create"),
    path('<int:pk>', RecruitmentDetailView.as_view(), name="recruitment-detail"),
    path('<int:pk>/update/', RecruitmentUpdateView.as_view(),
         name='recruitment-update'),
    path('<int:pk>/delete/', RecruitmentDeleteView.as_view(),
         name='recruitment-delete'),

]
