# Generated by Django 5.0.6 on 2024-08-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0013_alter_wishlist_wish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wish_price',
            field=models.FloatField(null=True),
        ),
    ]
