from django.contrib import admin
from django.urls import path
from sample_model import views
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from rest_framework_api_key.models import APIKey

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("api/sample-test", views.sample_model_viewer, name="sample-test"),
]

admin.site.site_header = "Aurora Forms"
admin.site.site_title = "Aurora Forms"
admin.site.index_title = "Bem-vindo ao painel Aurora Forms"
User._meta.verbose_name = _("Usuário")
User._meta.verbose_name_plural = _("Usuários")
Group._meta.verbose_name = _("Grupo")
Group._meta.verbose_name_plural = _("Grupos")
APIKey._meta.verbose_name = _("Chave de API")
APIKey._meta.verbose_name_plural = _("Chaves de API")
