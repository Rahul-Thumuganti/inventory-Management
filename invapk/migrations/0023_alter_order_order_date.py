# Generated by Django 4.2.6 on 2023-10-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0022_alter_product_supplier_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
