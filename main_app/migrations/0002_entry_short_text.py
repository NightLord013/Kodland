# Generated by Django 2.1.9 on 2020-07-31 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='short_text',
            field=models.CharField(default='', max_length=350, verbose_name='Краткая информация'),
        ),
    ]
