# Generated by Django 3.2.9 on 2022-02-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_utils', '0002_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
