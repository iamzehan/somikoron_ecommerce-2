# Generated by Django 3.0.7 on 2020-07-05 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20200705_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='subcategory',
            new_name='sub_category',
        ),
    ]
