from django.db import models  # type: ignore
from django import forms  # type: ignore


class QuestionModelChoices(models.TextChoices):
    R0 = "text_field", "Campo de texto"
    R1 = "multiple_choices", "Multipla escolha"
    R2 = "star_rate", "Avaliação com estrelas"
    R3 = "select_box", "Caixas de seleção"


class Question(models.Model):
    title = models.CharField(
        max_length=255, default="", null=False, verbose_name="Título"
    )

    question_model = models.CharField(
        choices=QuestionModelChoices.choices,
        max_length=110,
        blank=True,
        null=True,
        verbose_name="Modelo da pergunta",
    )

    min_text = models.CharField(
        max_length=100,
        default="Não gostei",
        null=False,
        verbose_name="Texto mínimo",
    )
    max_text = models.CharField(
        max_length=100,
        default="Gostei muito",
        null=False,
        verbose_name="Texto máximo",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pergunta"


class Option(models.Model):
    question = models.ForeignKey(
        Question, related_name="options", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Alternativa"

    def __str__(self):
        return self.text
