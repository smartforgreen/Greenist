# Generated by Django 4.1.7 on 2023-04-11 23:12

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0025_remove_mypolygon_fwi_remove_mypolygon_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypolygon',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
