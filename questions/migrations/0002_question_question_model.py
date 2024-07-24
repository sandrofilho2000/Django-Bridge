# Generated by Django 4.2.14 on 2024-07-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_model',
            field=models.CharField(blank=True, choices=[('text_field', 'Campo de texto'), ('multiple_choices', 'Multipla escolha'), ('star_rate', 'Avaliação com estrelas')], max_length=110, null=True),
        ),
    ]