# Generated by Django 3.0.7 on 2020-07-02 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200702_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_note',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]