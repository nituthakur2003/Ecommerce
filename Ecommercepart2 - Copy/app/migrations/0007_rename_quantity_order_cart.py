# Generated by Django 4.2.7 on 2024-01-26 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_quantities_order_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quantity',
            new_name='cart',
        ),
    ]
