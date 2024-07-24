from django.contrib import admin

from questions.models import Option, Question
from django.utils.translation import gettext_lazy as _


class CustomAdminSite(admin.AdminSite):
    site_header = _("My Custom Admin Header")
    site_title = _("My Custom Admin Title")
    index_title = _("Welcome to My Custom Admin Site")


admin_site = CustomAdminSite(name="custom_admin")


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "question_model"]
    inlines = [OptionInline]


admin.site.register(Question, QuestionAdmin)
