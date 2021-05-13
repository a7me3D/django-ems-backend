
from django.contrib import admin
from django.urls import path, include
from users.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', HomeView.as_view(), name="home"),
    path('', HomeView.as_view()),
    path('auth/', include("django.contrib.auth.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('users/', include("users.urls", namespace="users")),
    path('formations/', include("formations.urls", namespace="formations")),
    path('recruitments/', include("recruitments.urls", namespace="recruitments")),
    path('evaluations/', include("evaluations.urls", namespace="evaluations")),
    path('finances/', include("finance.urls", namespace="finances")),
    path('conges/', include("conges.urls", namespace="conges"))
]
