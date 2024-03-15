# Generated by Django 5.0.1 on 2024-02-05 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0007_bedavailability'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('specialization', models.CharField(choices=[('General Physician', 'General Physician'), ('Cardiologist', 'Cardiologist'), ('Surgeon', 'Surgeon'), ('Dermatologist', 'Dermatologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Pediatrician', 'Pediatrician')], max_length=50)),
                ('available_days', models.CharField(max_length=100)),
                ('timings', models.CharField(max_length=100)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.hospital')),
            ],
        ),
    ]
