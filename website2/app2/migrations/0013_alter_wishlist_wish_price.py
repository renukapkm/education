# Generated by Django 5.0.6 on 2024-08-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0012_alter_order_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wish_price',
            field=models.FloatField(),
        ),
    ]
