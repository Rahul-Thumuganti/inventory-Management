# Generated by Django 4.2.5 on 2023-10-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField(blank=True, db_index=True, default=0, help_text='Enter an integer value', null=True, unique=True, verbose_name='My Integer Field')),
                ('balance', models.DecimalField(decimal_places=6, max_digits=15)),
            ],
        ),
    ]