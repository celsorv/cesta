# Generated by Django 4.0.5 on 2022-06-15 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidadeorganizacao',
            name='metaQtdeCestas',
        ),
    ]
