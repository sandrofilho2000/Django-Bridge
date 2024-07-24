from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=100, default="", null=False, verbose_name="Nome")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Formulário"
