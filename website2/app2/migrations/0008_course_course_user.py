# Generated by Django 5.0.6 on 2024-07-25 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_user',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
