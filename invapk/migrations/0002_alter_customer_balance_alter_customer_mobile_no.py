# Generated by Django 4.2.5 on 2023-10-15 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_no',
            field=models.CharField(max_length=100),
        ),
    ]