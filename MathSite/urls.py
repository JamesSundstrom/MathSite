from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("problems/", include("problems.urls")),
    path("admin/", admin.site.urls),
]