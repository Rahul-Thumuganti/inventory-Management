# Generated by Django 4.2.6 on 2023-10-29 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invapk', '0013_alter_brand_b_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invapk.category'),
        ),
    ]
