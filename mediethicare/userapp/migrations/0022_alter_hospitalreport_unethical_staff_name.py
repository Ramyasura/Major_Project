# Generated by Django 5.0.1 on 2024-02-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0021_alter_appointment_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalreport',
            name='unethical_staff_name',
            field=models.CharField(blank=True, default='user', max_length=100, null=True),
        ),
    ]