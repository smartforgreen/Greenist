# Generated by Django 4.1.7 on 2023-04-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0022_alter_node_rssi'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='camera',
            field=models.BigIntegerField(null=True),
        ),
    ]
