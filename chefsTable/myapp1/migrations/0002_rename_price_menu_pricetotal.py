# Generated by Django 4.2.10 on 2024-03-12 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='price',
            new_name='priceTotal',
        ),
    ]
