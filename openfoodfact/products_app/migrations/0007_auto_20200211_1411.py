# Generated by Django 3.0b1 on 2020-02-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0006_auto_20200121_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fat_100g',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='salt_100g',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='saturated_fat_100g',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sugars_100g',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
