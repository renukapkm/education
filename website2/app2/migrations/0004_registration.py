# Generated by Django 5.0.6 on 2024-07-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_rename_contact_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_email', models.EmailField(max_length=255)),
                ('reg_password', models.CharField(max_length=255)),
                ('reg_username', models.CharField(max_length=255)),
                ('reg_phnum', models.CharField(max_length=255)),
            ],
        ),
    ]
