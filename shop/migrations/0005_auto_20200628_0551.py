# Generated by Django 3.0.7 on 2020-06-27 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_itemdetails_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Items', unique=True),
        ),
    ]
