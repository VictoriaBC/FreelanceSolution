# Generated by Django 3.0.8 on 2020-07-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_type',
            field=models.CharField(choices=[('ICON', 'Icon'), ('LOGO', 'Logo'), ('POSTER', 'Poster')], max_length=15),
        ),
    ]
