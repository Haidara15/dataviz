# Generated by Django 5.0.6 on 2024-06-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0014_remove_highchartdata_legend_align'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highchartdata',
            name='legend_layout',
        ),
        migrations.AlterField(
            model_name='highchartdata',
            name='show_legend',
            field=models.BooleanField(default=False),
        ),
    ]
