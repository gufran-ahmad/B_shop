# Generated by Django 3.2.8 on 2022-07-31 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='first_name',
            new_name='name',
        ),
    ]
