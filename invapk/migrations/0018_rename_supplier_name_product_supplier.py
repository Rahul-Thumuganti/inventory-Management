# Generated by Django 4.2.6 on 2023-10-30 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0017_rename_supplier_product_supplier_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='supplier_name',
            new_name='supplier',
        ),
    ]
