# Generated by Django 4.2.6 on 2023-12-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_alter_masterdata_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
