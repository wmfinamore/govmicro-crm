# Generated by Django 4.1 on 2022-08-24 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0006_unidade_funcionarios'),
        ('ocorrencias', '0004_historicalocorrencia_ano_ocorrencia_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='unidade_atual',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='unidades.unidade'),
        ),
    ]
