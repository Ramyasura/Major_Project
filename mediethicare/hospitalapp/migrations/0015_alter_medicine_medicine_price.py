# Generated by Django 5.0.1 on 2024-02-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0014_alter_bkmodel_medicine_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_price',
            field=models.CharField(max_length=100),
        ),
    ]
