# Generated by Django 5.0.6 on 2024-05-28 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0004_theme_remove_highchartdata_labels_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartvalue',
            name='highchart',
        ),
        migrations.AddField(
            model_name='highchartdata',
            name='labels',
            field=models.TextField(default='labels'),
        ),
        migrations.AddField(
            model_name='highchartdata',
            name='values',
            field=models.TextField(default='25'),
        ),
        migrations.AlterField(
            model_name='highchartdata',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charts', to='json_app.theme'),
        ),
        migrations.DeleteModel(
            name='ChartLabel',
        ),
        migrations.DeleteModel(
            name='ChartValue',
        ),
    ]
