# Generated by Django 2.2 on 2019-04-13 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20190413_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.CharField(max_length=50, verbose_name='Data Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fim',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_fim',
            field=models.TimeField(max_length=50, verbose_name='Fim Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_inicio',
            field=models.TimeField(max_length=50, verbose_name='Inico Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='inicio',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Inicio'),
        ),
    ]
