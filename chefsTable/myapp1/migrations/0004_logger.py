# Generated by Django 4.2.10 on 2024-03-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_menucategory_rename_cuisine_menu_menu_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('time_log', models.TimeField(help_text='Enter the exact time')),
            ],
        ),
    ]
