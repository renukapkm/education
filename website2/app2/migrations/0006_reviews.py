# Generated by Django 5.0.6 on 2024-07-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_course_cou_descri_course_cou_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_name', models.CharField(max_length=255)),
                ('rev_img', models.FileField(null=True, upload_to='student')),
                ('rev_text', models.TextField(null=True)),
            ],
        ),
    ]
