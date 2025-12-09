from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Endpoints da API do app cinema
    path("api/", include("cinema.urls")),
]
