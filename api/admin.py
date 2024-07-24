from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class CustomUser(User):
    class Meta:
        proxy = True
        app_label = "auth"
        verbose_name = _("My Custom User")


admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)
