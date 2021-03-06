# Generated by Django 3.0.7 on 2020-07-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20200718_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='apartment_and_house',
        ),
        migrations.RemoveField(
            model_name='address',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street_address',
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(default='Dhaka', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('PLACED', 'Order Placed'), ('RECEIVED', 'Order Received'), ('SHIPPING', 'Order is on the way'), ('DONE', 'Order Completed'), ('CANCELED', 'Order Canceled')], default='RECEIVED', max_length=20),
        ),
    ]
