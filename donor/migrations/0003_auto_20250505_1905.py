# Generated by Django 3.2.25 on 2025-05-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20210213_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
