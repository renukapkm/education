# Generated by Django 5.0.6 on 2024-07-25 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0008_course_course_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_amount',
        ),
    ]
