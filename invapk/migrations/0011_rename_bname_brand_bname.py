# Generated by Django 4.2.6 on 2023-10-29 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0010_rename_bname_brand_bname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='Bname',
            new_name='bname',
        ),
    ]
