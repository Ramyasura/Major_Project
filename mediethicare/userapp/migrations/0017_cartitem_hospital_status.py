# Generated by Django 5.0.1 on 2024-02-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0016_pendingmedicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='hospital_status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
