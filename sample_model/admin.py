from django.contrib import admin
from sample_model.models import SampleModel


class SampleModelAdmin(admin.ModelAdmin):
    list_display = [
        "sample_field",
    ]
