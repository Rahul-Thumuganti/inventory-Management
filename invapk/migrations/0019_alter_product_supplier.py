# Generated by Django 4.2.6 on 2023-10-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0018_rename_supplier_name_product_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=100),
        ),
    ]