# Generated by Django 5.0.6 on 2024-05-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highchartdata',
            name='labels',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='highchartdata',
            name='values',
            field=models.TextField(),
        ),
    ]
