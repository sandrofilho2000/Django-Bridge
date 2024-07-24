from django.contrib import admin

from forms.models import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ["name"]
