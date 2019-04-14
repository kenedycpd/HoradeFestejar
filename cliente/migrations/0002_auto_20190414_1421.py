# Generated by Django 2.2 on 2019-04-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='cpf',
            field=models.CharField(default=1, max_length=15, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
    ]