# Generated by Django 4.2.6 on 2023-10-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0004_alter_customer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='min_ord',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]