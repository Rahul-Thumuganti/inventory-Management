# Generated by Django 4.2.6 on 2023-10-30 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0020_product_supplier_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
