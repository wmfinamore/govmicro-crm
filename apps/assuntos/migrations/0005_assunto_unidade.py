# Generated by Django 4.1 on 2022-08-24 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0006_unidade_funcionarios'),
        ('assuntos', '0004_alter_assunto_folha'),
    ]

    operations = [
        migrations.AddField(
            model_name='assunto',
            name='unidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='unidades.unidade'),
        ),
    ]
