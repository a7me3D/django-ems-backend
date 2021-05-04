
from django.contrib import admin
from django.urls import path, include
from users.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', HomeView.as_view()),
    path('', HomeView.as_view()),
    path('auth/', include("django.contrib.auth.urls")),
    path('users/', include("users.urls", namespace="users")),
    path('formations/', include("formations.urls", namespace="formations"))
]
