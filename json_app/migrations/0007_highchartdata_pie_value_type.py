# Generated by Django 5.0.6 on 2024-06-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0006_highchartdata_modified_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='highchartdata',
            name='pie_value_type',
            field=models.CharField(choices=[('Nombre', 'Nombre'), ('Pourcentage', 'Pourcentage')], default='Nombre', max_length=20),
        ),
    ]
