from typing import Required
from django.db import models


class SampleModel(models.Model):
    sample_field = models.CharField(
        max_length=100, verbose_name="Sample field", null=False, default="Hello, world!"
    )

    class Meta:
        verbose_name = "Sample model"
        verbose_name_plural = "Sample models"

    def __str__(self):
        return self.sample_field
