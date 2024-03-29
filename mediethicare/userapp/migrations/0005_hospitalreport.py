# Generated by Django 5.0.1 on 2024-02-07 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0009_diagnosticservice_emergencyservice_surgicalservice'),
        ('userapp', '0004_appointment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('cancellation_reason_given', models.BooleanField()),
                ('cancellation_inform', models.BooleanField()),
                ('unethical_staff_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bill_upload', models.FileField(blank=True, null=True, upload_to='hospital_reports/')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]
