# Generated by Django 4.1 on 2022-08-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assuntos', '0002_remove_assunto_data_alteracao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assunto',
            name='folha',
            field=models.BooleanField(default=True),
        ),
    ]
