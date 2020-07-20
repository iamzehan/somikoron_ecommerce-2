# Generated by Django 3.0.7 on 2020-07-18 11:36

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattleinfo',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cattle', to='shop.Items'),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item_details', to='shop.Items'),
        ),
        migrations.AlterField(
            model_name='itemimages',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='media/images/'),
        ),
    ]