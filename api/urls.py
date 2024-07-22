from django.contrib import admin
from django.urls import path
from sample_model import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("api/sample-test", views.sample_model_viewer, name="sample-test"),
]
